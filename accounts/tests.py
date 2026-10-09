from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertContains(response, "Login")

    def test_login_page_contains_authentication_form(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context["form"],
            AuthenticationForm,
        )

    def test_login_page_displays_login_form(self):
        response = self.client.get(reverse("login"))

        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')
        self.assertContains(response, 'type="submit"')

    def test_valid_credentials_log_user_in(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "TestPassword123!",
            }
        )

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_credentials_do_not_log_user_in(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "WrongPassword123!",
            },
        )

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_redirects_to_home(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "TestPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("home"),
        )

    def test_logout_ends_authenticated_session(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("logout"))

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(
            response,
            reverse("home"),
        )


class RegistrationViewTests(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse("register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "accounts/register.html",
        )
        self.assertIsInstance(
            response.context["form"],
            UserCreationForm,
        )
        self.assertContains(response, "Register")

    def test_valid_registration_creates_user(self):
        user_model = get_user_model()

        response = self.client.post(
            reverse("register"),
            {
                "username": "newcustomer",
                "password1": "SecureTestPassword123!",
                "password2": "SecureTestPassword123!",
            },
        )

        self.assertEqual(
            user_model.objects.filter(username="newcustomer").count(),
            1,
        )

    def test_registration_rejects_mismatched_passwords(self):
        user_model = get_user_model()

        response = self.client.post(
            reverse("register"),
            {
                "username": "newcustomer",
                "password1": "SecureTestPassword123!",
                "password2": "DifferentPassword123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            user_model.objects.filter(username="newcustomer").exists()
        )
        self.assertContains(
            response,
            "The two password fields didn’t match.",
        )

    def test_registration_rejects_duplicate_username(self):
        user_model = get_user_model()

        user_model.objects.create_user(
            username="existingcustomer",
            password="SecureTestPassword123!",
        )

        response = self.client.post(
            reverse("register"),
            {
                "username": "existingcustomer",
                "password1": "AnotherSecurePassword123!",
                "password2": "AnotherSecurePassword123!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            user_model.objects.filter(
                username="existingcustomer"
            ).count(),
            1,
        )
        self.assertContains(
            response,
            "A user with that username already exists.",
        )

    def test_successful_registration_redirects_to_login(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newcustomer",
                "password1": "SecureTestPassword123!",
                "password2": "SecureTestPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("login"),
        )