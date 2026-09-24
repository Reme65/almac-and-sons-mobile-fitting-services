import re

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

    def clean_occupant_safety(self):
        occupant_safety = self.cleaned_data["occupant_safety"]

        allowed_values = {
            "yes",
            "no",
            "unsure",
        }

        if occupant_safety not in allowed_values:
            raise forms.ValidationError(
                "Please select a valid occupant safety option."
            )

        return occupant_safety
    def clean_occupant_count(self):
        occupant_count = self.cleaned_data["occupant_count"]

        if not 0 <= occupant_count <= 99:
            raise forms.ValidationError(
                "Occupant count must be between 0 and 99."
            )

        return occupant_count

    def clean_contact_phone(self):
        phone_number = self.cleaned_data["contact_phone"]

        if not re.fullmatch(r"\+?[0-9()\s-]+", phone_number):
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        digit_count = sum(character.isdigit() for character in phone_number)

        if not 7 <= digit_count <= 15:
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone_number

    def clean_location_postcode(self):
        postcode = self.cleaned_data["location_postcode"]

        if not postcode:
            return postcode

        postcode_pattern = (
            r"^(?:GIR\s?0AA|"
            r"(?:[A-Z]{1,2}[0-9][A-Z0-9]?)\s?[0-9][A-Z]{2})$"
        )

        if not re.fullmatch(
            postcode_pattern,
            postcode,
            flags=re.IGNORECASE,
        ):
            raise forms.ValidationError(
                "Please enter a valid UK postcode."
            )

        return postcode
    