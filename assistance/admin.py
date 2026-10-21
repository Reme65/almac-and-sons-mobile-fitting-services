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
