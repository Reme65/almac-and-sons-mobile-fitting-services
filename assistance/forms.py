from django import forms

from .models import AssistanceRequest


class AssistanceRequestForm(forms.ModelForm):
    class Meta:
        model = AssistanceRequest
        fields = [
            "vehicle_registration",
            "vehicle_type",
            "vehicle_make",
            "vehicle_model",
            "vehicle_description",
            "problem_type",
            "problem_description",
            "location_type",
            "location_postcode",
            "location_description",
            "location_direction",
            "location_access",
            "occupant_count",
            "assistance_needs",
            "assistance_details",
            "occupant_safety",
            "contact_first_name",
            "contact_last_name",
            "contact_phone",
            "contact_email",
            "contact_notes",
        ]




    def clean_vehicle_type(self):
        vehicle_type = self.cleaned_data["vehicle_type"]

        allowed_types = {
            "car",
            "van",
            "hgv",
            "trailer",
            "agricultural",
            "other",
        }

        if vehicle_type not in allowed_types:
            raise forms.ValidationError(
                "Please select a valid vehicle or equipment type."
            )

        return vehicle_type
