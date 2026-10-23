
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from assistance.models import AssistanceRequest
from .models import Payment


logger = logging.getLogger(__name__)


@login_required
@require_POST
def create_checkout_session(request, payment_id):
    payment = get_object_or_404(
        Payment,
        id=payment_id,
        assistance_request__customer=request.user,
        status=Payment.Status.PENDING,
    )
    if (
        payment.timing == Payment.Timing.ON_COMPLETION
        and payment.assistance_request.status != AssistanceRequest.Status.COMPLETED
    ):
        return HttpResponseBadRequest(
        "Payment is not due until assistance is completed."
       )

    if payment.amount <= 0:
        return HttpResponseBadRequest("Invalid payment amount.")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        checkout_session = stripe.checkout.Session.create(
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": int(payment.amount * 100),
                        "product_data": {
                            "name": "Almac & Sons Assistance",
                        },
                    },
                    "quantity": 1,
                }
            ],
            client_reference_id=str(payment.id),
            success_url=request.build_absolute_uri("/payments/success/"),
            cancel_url=request.build_absolute_uri("/payments/cancel/"),
        )

    except stripe.StripeError:
        logger.exception("Stripe Checkout session creation failed")
        return HttpResponse(
            "Payment service temporarily unavailable. Please try again later.",
            status=503,
        )

    payment.stripe_checkout_session_id = checkout_session.id
    payment.save(update_fields=["stripe_checkout_session_id"])

    return redirect(checkout_session.url)


@login_required
def payment_success(request):
    return HttpResponse(
        "You have returned from Stripe Checkout. "
        "Your payment is awaiting confirmation."
    )


@login_required
def payment_cancel(request):
    return HttpResponse(
        "You have cancelled Stripe Checkout. "
        "No payment has been confirmed."
    )


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    signature = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    if not settings.STRIPE_WEBHOOK_SECRET:
        return HttpResponse(
            "Webhook is not configured.",
            status=503,
        )

    try:
        event = stripe.Webhook.construct_event(
            payload,
            signature,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except (ValueError, stripe.SignatureVerificationError):
        return HttpResponseBadRequest("Invalid webhook signature.")

    logger.info("Verified Stripe event: %s", event["type"])
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        if hasattr(session, "to_dict"):
            session = session.to_dict()

        if session.get("payment_status") == "paid":
            logger.info(
                "Stripe confirmed payment for session: %s",
                session.get("id"),
            )

            payment = Payment.objects.filter(
                stripe_checkout_session_id=session.get("id"),
                pk=session.get("client_reference_id"),
            ).first()

            if payment and payment.status == Payment.Status.PENDING:
                payment.status = Payment.Status.PAID
                payment.paid_at = timezone.now()
                payment.stripe_payment_intent_id = (
                     session.get("payment_intent") or ""
                )
                payment.save()

    return HttpResponse(status=200)
