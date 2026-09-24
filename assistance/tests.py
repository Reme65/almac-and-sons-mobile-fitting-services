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
class AssistanceNeedsValidationTests(SimpleTestCase):

    def test_valid_assistance_needs_are_accepted(self):
        allowed_values = [
            "yes",
            "no",
            "unsure",
        ]

        for assistance_needs in allowed_values:
            with self.subTest(assistance_needs=assistance_needs):
                form = AssistanceRequestForm()
                form.cleaned_data = {
                    "assistance_needs": assistance_needs
                }

                self.assertEqual(
                    form.clean_assistance_needs(),
                    assistance_needs,
                )

    def test_invalid_assistance_needs_are_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {
            "assistance_needs": "spaceship"
        }

        with self.assertRaisesMessage(
            ValidationError,
            "Please select a valid assistance needs option.",
        ):
            form.clean_assistance_needs()  

class OccupantSafetyValidationTests(SimpleTestCase):

    def test_valid_occupant_safety_values_are_accepted(self):
        allowed_values = [
            "yes",
            "no",
            "unsure",
        ]

        for occupant_safety in allowed_values:
            with self.subTest(occupant_safety=occupant_safety):
                form = AssistanceRequestForm()
                form.cleaned_data = {
                    "occupant_safety": occupant_safety
                }

                self.assertEqual(
                    form.clean_occupant_safety(),
                    occupant_safety,
                )

    def test_invalid_occupant_safety_value_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {
            "occupant_safety": "spaceship"
        }

        with self.assertRaisesMessage(
            ValidationError,
            "Please select a valid occupant safety option.",
        ):
            form.clean_occupant_safety()
                   