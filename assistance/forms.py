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

    def clean_problem_type(self):
        problem_type = self.cleaned_data["problem_type"]

        allowed_types = {
            "wont-start",
            "flat-tyre",
            "breakdown",
            "recovery",
            "other",
            "unsure",
        }

        if problem_type not in allowed_types:
            raise forms.ValidationError(
                "Please select a valid problem type."
            )

        return problem_type

    def clean_location_type(self):
        location_type = self.cleaned_data["location_type"]

        allowed_types = {
            "roadside",
            "motorway",
            "home",
            "workplace",
            "other",
        }

        if location_type not in allowed_types:
            raise forms.ValidationError(
                "Please select a valid location type."
            )

        return location_type

    def clean_assistance_needs(self):
        assistance_needs = self.cleaned_data["assistance_needs"]

        allowed_values = {
            "yes",
            "no",
            "unsure",
        }

        if assistance_needs not in allowed_values:
            raise forms.ValidationError(
                "Please select a valid assistance needs option."
            )

        return assistance_needs
    