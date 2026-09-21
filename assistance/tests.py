from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from .forms import AssistanceRequestForm


class VehicleTypeValidationTests(SimpleTestCase):

    def test_valid_vehicle_type_is_accepted(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"vehicle_type": "car"}

        self.assertEqual(form.clean_vehicle_type(), "car")

    def test_invalid_vehicle_type_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"vehicle_type": "spaceship"}

        with self.assertRaisesMessage(
            ValidationError,
            "Please select a valid vehicle or equipment type.",
        ):
            form.clean_vehicle_type()
            