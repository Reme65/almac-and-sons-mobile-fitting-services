from django.test import TestCase
from django.urls import reverse


class ServicesViewTests(TestCase):

    def test_services_page_renders_services_template(self):
        response = self.client.get(reverse("services"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services.html")
        self.assertContains(
            response,
            f'href="{reverse("home")}"',
        )
        self.assertContains(
            response,
            f'href="{reverse("services")}"',
        )
        self.assertContains(
            response,
            f'href="{reverse("home")}#how-it-works"',
        )
