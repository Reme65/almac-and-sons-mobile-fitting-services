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

class ProblemTypeValidationTests(SimpleTestCase):

    def test_valid_problem_types_are_accepted(self):
        allowed_types = [
            "wont-start",
            "flat-tyre",
            "breakdown",
            "recovery",
            "other",
            "unsure",
        ]

        for problem_type in allowed_types:
            with self.subTest(problem_type=problem_type):
                form = AssistanceRequestForm()
                form.cleaned_data = {"problem_type": problem_type}

                self.assertEqual(
                    form.clean_problem_type(),
                    problem_type,
                )

    def test_invalid_problem_type_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"problem_type": "spaceship"}

        with self.assertRaisesMessage(
            ValidationError,
            "Please select a valid problem type.",
        ):
            form.clean_problem_type()
class LocationTypeValidationTests(SimpleTestCase):

    def test_valid_location_types_are_accepted(self):
        allowed_types = [
            "roadside",
            "motorway",
            "home",
            "workplace",
            "other",
        ]

        for location_type in allowed_types:
            with self.subTest(location_type=location_type):
                form = AssistanceRequestForm()
                form.cleaned_data = {"location_type": location_type}

                self.assertEqual(
                    form.clean_location_type(),
                    location_type,
                )

    def test_invalid_location_type_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"location_type": "spaceship"}

        with self.assertRaisesMessage(
            ValidationError,
            "Please select a valid location type.",
        ):
            form.clean_location_type()
            