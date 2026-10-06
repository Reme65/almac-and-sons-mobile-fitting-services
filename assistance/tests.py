from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

import uuid
from .forms import AssistanceRequestForm
from .models import AssistanceRequest

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

    def test_missing_location_description_is_rejected(self):
        form_data = self.get_valid_form_data()
        form_data["location_description"] = ""

        form = AssistanceRequestForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("location_description", form.errors)

    def test_missing_contact_phone_is_rejected(self):
        form_data = self.get_valid_form_data()
        form_data["contact_phone"] = ""

        form = AssistanceRequestForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("contact_phone", form.errors)

    def test_blank_contact_email_is_accepted(self):
        form_data = self.get_valid_form_data()
        form_data["contact_email"] = ""

        form = AssistanceRequestForm(data=form_data)

        self.assertTrue(form.is_valid(), form.errors.as_json())           

    def test_invalid_contact_email_is_rejected(self):
        form_data = self.get_valid_form_data()
        form_data["contact_email"] = "not-an-email"

        form = AssistanceRequestForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("contact_email", form.errors)

class AssistanceRequestViewTests(TestCase):

    def test_valid_post_creates_assistance_request(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

    def test_invalid_post_does_not_create_assistance_request(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["problem_description"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn("form", response.context)
        self.assertIn(
            "problem_description",
            response.context["form"].errors,
        )
        self.assertContains(
            response,
            "This field is required.",
        )
        self.assertEqual(
            response.context["error_step"],
            2,
        )

    def test_invalid_postcode_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        ) 
        form_data["location_postcode"] = "12345"

        response = self.client.post(
             reverse("request_assistance"),
             data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "location_postcode",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            3,
        )
        self.assertContains(
            response,
            "Please enter a valid UK postcode.",
        )

    def test_invalid_phone_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["contact_phone"] = "not-a-phone-number"

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "contact_phone",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            5,
        )
        self.assertContains(
            response,
            "Please enter a valid phone number.",
        )

    def test_invalid_email_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["contact_email"] = "not-an-email"

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "contact_email",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            5,
        )
        self.assertContains(
            response,
            "Enter a valid email address.",
        )

    def test_invalid_occupant_count_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["occupant_count"] = "100"

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "occupant_count",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            4,
        )
        self.assertContains(
            response,
            "Occupant count must be between 0 and 99.",
        )

    def test_missing_vehicle_type_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["vehicle_type"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "vehicle_type",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            1,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_missing_problem_type_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["problem_type"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "problem_type",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            2,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_missing_location_type_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["location_type"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "location_type",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            3,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_missing_location_description_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["location_description"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "location_description",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            3,
        )
        self.assertContains(
            response,
            "This field is required.",
        )  

    def test_missing_assistance_needs_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["assistance_needs"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "assistance_needs",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            4,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_missing_occupant_safety_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["occupant_safety"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "occupant_safety",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            4,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_missing_contact_first_name_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["contact_first_name"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "contact_first_name",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            5,
        )
        self.assertContains(
            response,
            "This field is required.",
        ) 
    def test_missing_contact_last_name_error_is_displayed(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["contact_last_name"] = ""

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn(
            "contact_last_name",
            response.context["form"].errors,
        )
        self.assertEqual(
            response.context["error_step"],
            5,
        )
        self.assertContains(
            response,
            "This field is required.",
        )

    def test_confirmation_page_returns_404_for_unknown_reference(self):
        unknown_reference = uuid.uuid4()

        response = self.client.get(
            reverse(
                "assistance_confirmation",
                kwargs={"reference": unknown_reference},
            )
        )

        self.assertEqual(response.status_code, 404)       

    def test_invalid_post_preserves_vehicle_registration(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )
        form_data["vehicle_registration"] = "AB12 CDE"
        form_data["location_postcode"] = "12345"

        response = self.client.post(
             reverse("request_assistance"),
             data=form_data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'value="AB12 CDE"',
        )

    def test_valid_post_redirects_to_confirmation_page(self):
        form_data = (
            CompleteAssistanceRequestFormTests()
            .get_valid_form_data()
        )

        response = self.client.post(
            reverse("request_assistance"),
            data=form_data,
        )

        saved_request = AssistanceRequest.objects.get()

        self.assertRedirects(
        response,
        reverse(
            "assistance_confirmation",
            kwargs={"reference": saved_request.reference},
        ),
    )

class AssistanceConfirmationViewTests(TestCase):

    def test_confirmation_page_displays_saved_request(self):
        assistance_request = AssistanceRequest.objects.create(
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Engine stopped.",
            location_type="roadside",
            location_description="A350 lay-by",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="Test",
            contact_last_name="Customer",
            contact_phone="07123456789",
        )

        response = self.client.get(
            reverse(
                "assistance_confirmation",
                kwargs={"reference": assistance_request.reference},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "assistance-confirmation.html",
        )
        self.assertEqual(
            response.context["assistance_request"],
            assistance_request,
        )

class AssistanceConfirmationTemplateTests(SimpleTestCase):

    def test_confirmation_template_renders(self):
        from django.template.loader import render_to_string

        html = render_to_string("assistance-confirmation.html")

        self.assertIn("Request Received", html)
        self.assertIn(
            "Your request for assistance has been submitted",
            html,
        )
        self.assertIn("What happens next?", html)
        self.assertIn("We assess your request", html)
        self.assertIn("We arrange assistance", html)
        self.assertIn("We provide an estimated arrival time", html)
        self.assertIn("We keep you updated", html)
        self.assertIn("Keep your phone available", html)
        self.assertIn(
            "We may need to contact you about your assistance request",
            html,
        )
        self.assertIn("Are you in immediate danger?", html)
        self.assertIn("999", html)

    def test_confirmation_has_action_links(self):
        from django.template.loader import render_to_string

        html = render_to_string("assistance-confirmation.html")

        self.assertIn(
            f'href="{reverse("home")}"',
            html,
        )
        self.assertIn("Return to Home", html)
        self.assertIn(
            f'href="{reverse("services")}"',
            html,
        )
        self.assertIn("View Services", html)
        