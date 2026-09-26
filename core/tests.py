from django.test import TestCase
from django.urls import reverse


class ServicesViewTests(TestCase):

    def test_services_page_renders_services_template(self):
        response = self.client.get(reverse("services"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services.html")
        