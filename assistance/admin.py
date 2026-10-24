from django.contrib import admin

from .models import AssistanceRequest


@admin.register(AssistanceRequest)
class AssistanceRequestAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "contact_first_name",
        "contact_last_name",
        "vehicle_registration",
        "status",
        "payment_summary",
        "created_at",
    )
    list_filter = (
        "status",
    )
    search_fields = (
        "reference",
        "contact_first_name",
        "contact_last_name",
        "vehicle_registration",
        "contact_phone",
    )

    @admin.display(description="Payments")
    def payment_summary(self, obj):
        payments = obj.payments.all()

        paid = sum(
            payment.status == "paid"
            for payment in payments
        )

        pending = sum(
            payment.status == "pending"
            for payment in payments
        )

        return f"{paid} paid / {pending} pending"
