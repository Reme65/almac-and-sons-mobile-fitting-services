
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

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

    if payment.amount <= 0:
        return HttpResponseBadRequest("Invalid payment amount.")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        checkout_session = stripe.checkout.Session.create(
            mode="payment",
            payment_method_types=["card"],
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

    return HttpResponse(status=200)
