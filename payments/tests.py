
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from unittest.mock import patch

import stripe
from django.contrib.auth import get_user_model
from django.test import RequestFactory

from .views import create_checkout_session
from assistance.models import AssistanceRequest
from .models import Payment


class PaymentModelTests(TestCase):
    def test_payment_defaults(self):
        assistance_request = AssistanceRequest.objects.create(
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Engine will not start",
            location_type="roadside",
            location_description="Supermarket car park",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="John",
            contact_last_name="Smith",
            contact_phone="07123456789",
        )

        payment = Payment.objects.create(
            assistance_request=assistance_request,
            amount=Decimal("75.00"),
        )

        self.assertEqual(payment.amount, Decimal("75.00"))
        self.assertEqual(payment.status, Payment.Status.PENDING)
        self.assertEqual(payment.timing, Payment.Timing.ON_COMPLETION)
        self.assertEqual(payment.assistance_request, assistance_request)

    def test_payment_rejects_zero_amount(self):
        payment = Payment(
            amount=Decimal("0.00"),
        )

        with self.assertRaises(ValidationError):
            payment.full_clean()


class StripeCheckoutViewTests(TestCase):
    def test_stripe_failure_returns_503(self):
        user = get_user_model().objects.create_user(
            username="stripecustomer",
            password="TestPassword123!",
        )

        assistance_request = AssistanceRequest.objects.create(
            customer=user,
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Engine will not start",
            location_type="roadside",
            location_description="Supermarket car park",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="John",
            contact_last_name="Smith",
            contact_phone="07123456789",
        )

        payment = Payment.objects.create(
            assistance_request=assistance_request,
            amount=Decimal("75.00"),
        )

        request = RequestFactory().post("/payments/checkout/")
        request.user = user

        with patch(
            "payments.views.stripe.checkout.Session.create",
            side_effect=stripe.StripeError("Simulated Stripe failure"),
        ):
            response = create_checkout_session(request, payment.id)

        self.assertEqual(response.status_code, 503)
        self.assertEqual(payment.status, Payment.Status.PENDING)

    def test_webhook_rejects_missing_secret(self):
        with self.settings(STRIPE_WEBHOOK_SECRET=""):
            response = self.client.post(
                "/payments/webhook/",
                data="{}",
                content_type="application/json",
            )

        self.assertEqual(response.status_code, 503)

    def test_webhook_rejects_invalid_signature(self):
        with self.settings(STRIPE_WEBHOOK_SECRET="whsec_test_secret"):
            response = self.client.post(
                "/payments/webhook/",
                data="{}",
                content_type="application/json",
                HTTP_STRIPE_SIGNATURE="invalid_signature",
            )

        self.assertEqual(response.status_code, 400)
