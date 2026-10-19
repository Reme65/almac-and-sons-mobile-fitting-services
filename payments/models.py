
from django.db import models
from assistance.models import AssistanceRequest


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    class Timing(models.TextChoices):
        UPFRONT = "upfront", "Upfront"
        ON_COMPLETION = "on_completion", "On completion"

    assistance_request = models.ForeignKey(
        AssistanceRequest,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    timing = models.CharField(
        max_length=20,
        choices=Timing.choices,
        default=Timing.ON_COMPLETION,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    stripe_checkout_session_id = models.CharField(
        max_length=255,
        blank=True,
    )

    stripe_payment_intent_id = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.assistance_request.reference} - £{self.amount}"
