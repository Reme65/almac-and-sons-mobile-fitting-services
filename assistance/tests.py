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

class OccupantCountValidationTests(SimpleTestCase):

    def test_valid_occupant_counts_are_accepted(self):
        for count in [0, 1, 5, 99]:
            with self.subTest(count=count):
                form = AssistanceRequestForm()
                form.cleaned_data = {"occupant_count": count}

                self.assertEqual(
                    form.clean_occupant_count(),
                    count,
                )

    def test_negative_occupant_count_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"occupant_count": -1}

        with self.assertRaisesMessage(
            ValidationError,
            "Occupant count must be between 0 and 99.",
        ):
            form.clean_occupant_count()

    def test_occupant_count_above_99_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"occupant_count": 100}

        with self.assertRaisesMessage(
            ValidationError,
            "Occupant count must be between 0 and 99.",
        ):
            form.clean_occupant_count()

class ContactPhoneValidationTests(SimpleTestCase):

    def test_valid_phone_numbers_are_accepted(self):
        valid_numbers = [
            "07123 456789",
            "020 7946 0123",
            "+44 7123 456789",
            "01234-567890",
            "(020) 7946 0123",
            "1234567",
            "123456789012345",
        ]

        for phone_number in valid_numbers:
            with self.subTest(phone_number=phone_number):
                form = AssistanceRequestForm()
                form.cleaned_data = {"contact_phone": phone_number}

                self.assertEqual(
                    form.clean_contact_phone(),
                    phone_number,
                )

    def test_invalid_phone_characters_are_rejected(self):
        invalid_numbers = [
            "07123 ABCDEF",
            "07123@456789",
            "07123+456789",
        ]

        for phone_number in invalid_numbers:
            with self.subTest(phone_number=phone_number):
                form = AssistanceRequestForm()
                form.cleaned_data = {"contact_phone": phone_number}

                with self.assertRaisesMessage(
                    ValidationError,
                    "Please enter a valid phone number.",
                ):
                    form.clean_contact_phone()

    def test_phone_number_with_too_few_digits_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"contact_phone": "123456"}

        with self.assertRaisesMessage(
            ValidationError,
            "Please enter a valid phone number.",
        ):
            form.clean_contact_phone()

    def test_phone_number_with_too_many_digits_is_rejected(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {
            "contact_phone": "1234567890123456"
        }

        with self.assertRaisesMessage(
            ValidationError,
            "Please enter a valid phone number.",
        ):
            form.clean_contact_phone()

class LocationPostcodeValidationTests(SimpleTestCase):

    def test_blank_postcode_is_accepted(self):
        form = AssistanceRequestForm()
        form.cleaned_data = {"location_postcode": ""}

        self.assertEqual(form.clean_location_postcode(), "")

    def test_valid_postcodes_are_accepted(self):
        valid_postcodes = [
            "BA14 8AA",
            "ba14 8aa",
            "SW1A 1AA",
            "M1 1AE",
            "B33 8TH",
            "CR2 6XH",
            "DN55 1PT",
            "GIR 0AA",
        ]

        for postcode in valid_postcodes:
            with self.subTest(postcode=postcode):
                form = AssistanceRequestForm()
                form.cleaned_data = {"location_postcode": postcode}

                self.assertEqual(
                    form.clean_location_postcode(),
                    postcode,
                )

    def test_invalid_postcodes_are_rejected(self):
        invalid_postcodes = [
            "12345",
            "ABCDE",
            "BA14",
            "BA14 8A",
            "BA14 8AAA",
            "BA14 @AA",
        ]

        for postcode in invalid_postcodes:
            with self.subTest(postcode=postcode):
                form = AssistanceRequestForm()
                form.cleaned_data = {"location_postcode": postcode}

                with self.assertRaisesMessage(
                    ValidationError,
                    "Please enter a valid UK postcode.",
                ):
                    form.clean_location_postcode()

class CompleteAssistanceRequestFormTests(SimpleTestCase):

    def get_valid_form_data(self):
        return {
            "vehicle_registration": "AB12 CDE",
            "vehicle_type": "car",
            "vehicle_make": "Ford",
            "vehicle_model": "Focus",
            "vehicle_description": "",
            "problem_type": "breakdown",
            "problem_description": "The engine stopped while driving.",
            "location_type": "roadside",
            "location_postcode": "BA14 8AA",
            "location_description": "Near the entrance to the retail park.",
            "location_direction": "",
            "location_access": "",
            "occupant_count": 2,
            "assistance_needs": "no",
            "assistance_details": "",
            "occupant_safety": "yes",
            "contact_first_name": "Alex",
            "contact_last_name": "Taylor",
            "contact_phone": "07123 456789",
            "contact_email": "alex@example.com",
            "contact_notes": "",
        }

    def test_complete_assistance_request_is_valid(self):
        form_data = self.get_valid_form_data()
        form = AssistanceRequestForm(data=form_data)

        self.assertTrue(form.is_valid(), form.errors.as_json())

    def test_missing_problem_description_is_rejected(self):
        form_data = self.get_valid_form_data()
        form_data["problem_description"] = ""

        form = AssistanceRequestForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("problem_description", form.errors)
        