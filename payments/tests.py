
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase

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
