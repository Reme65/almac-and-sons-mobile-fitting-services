
from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "assistance_request",
        "customer_name",
        "amount",
        "timing",
        "status",
        "created_at",
        "paid_at",
    )

    list_filter = (
        "status",
        "timing",
    )

    search_fields = (
        "assistance_request__reference",
    )

    readonly_fields = (
        "status",
        "stripe_checkout_session_id",
        "stripe_payment_intent_id",
        "created_at",
        "paid_at",
    )

    @admin.display(description="Customer")
    def customer_name(self, obj):
        request = obj.assistance_request
        return f"{request.contact_first_name} {request.contact_last_name}"
