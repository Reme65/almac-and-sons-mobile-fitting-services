from django.contrib.auth.forms import AuthenticationForm
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
