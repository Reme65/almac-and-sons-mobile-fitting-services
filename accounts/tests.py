from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse
from assistance.models import AssistanceRequest


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

    def test_login_redirects_to_requested_dashboard(self):
        user_model = get_user_model()

        user_model.objects.create_user(
            username="dashboardcustomer",
            password="SecureTestPassword123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "dashboardcustomer",
                "password": "SecureTestPassword123!",
                "next": reverse("dashboard"),
            },
        )

        self.assertRedirects(
            response,
            reverse("dashboard"),
        )

    def test_login_rejects_external_redirect(self):
        user_model = get_user_model()

        user_model.objects.create_user(
            username="securitycustomer",
            password="SecureTestPassword123!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "username": "securitycustomer",
                "password": "SecureTestPassword123!",
                "next": "https://example.com/unsafe",
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

        response = self.client.post(reverse("logout"))

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(
            response,
            reverse("home"),
        )

    def test_get_request_does_not_log_user_out(self):
        user_model = get_user_model()

        user = user_model.objects.create_user(
            username="logoutcustomer",
            password="SecureTestPassword123!",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 405)
        self.assertTrue(
            response.wsgi_request.user.is_authenticated
        )

    def test_authenticated_user_redirected_from_login(self):
        user_model = get_user_model()

        user = user_model.objects.create_user(
            username="loggedincustomer",
            password="SecureTestPassword123!",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("login"))

        self.assertRedirects(
            response,
            reverse("dashboard"),
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
        self.assertRedirects(response, reverse("login"))

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

    def test_authenticated_user_redirected_from_registration(self):
        user_model = get_user_model()

        user = user_model.objects.create_user(
            username="registeredcustomer",
            password="SecureTestPassword123!",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("register"))

        self.assertRedirects(
            response,
            reverse("dashboard"),
        )


class DashboardViewTests(TestCase):

    def test_dashboard_requires_login(self):
        response = self.client.get(
            reverse("dashboard")
        )

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("dashboard")}',
        )

    def test_dashboard_displays_only_own_requests(self):
        user_model = get_user_model()

        customer_a = user_model.objects.create_user(
            username="customer_a",
            password="SecureTestPassword123!",
        )

        customer_b = user_model.objects.create_user(
            username="customer_b",
            password="SecureTestPassword123!",
        )

        own_request = AssistanceRequest.objects.create(
            customer=customer_a,
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Flat battery",
            location_type="roadside",
            location_description="Supermarket car park",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="Customer",
            contact_last_name="A",
            contact_phone="07123456789",
        )

        other_request = AssistanceRequest.objects.create(
            customer=customer_b,
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Engine stopped",
            location_type="roadside",
            location_description="A350 lay-by",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="Customer",
            contact_last_name="B",
            contact_phone="07123456789",
        )

        self.client.force_login(customer_a)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(own_request.reference))
        self.assertNotContains(response, str(other_request.reference))

        self.assertQuerySetEqual(
            response.context["assistance_requests"],
            [own_request],
        )

    def test_dashboard_displays_message_when_no_requests(self):
        user_model = get_user_model()

        customer = user_model.objects.create_user(
            username="newcustomer",
            password="SecureTestPassword123!",
        )

        self.client.force_login(customer)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "You haven't submitted any assistance requests yet.",
        )
        self.assertQuerySetEqual(
            response.context["assistance_requests"],
            [],
        )


class StaffDashboardViewTests(TestCase):

    def test_staff_dashboard_requires_login(self):
        response = self.client.get(
            reverse("staff_dashboard")
        )

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("staff_dashboard")}',
        )

    def test_staff_dashboard_rejects_ordinary_customer(self):
        user_model = get_user_model()

        customer = user_model.objects.create_user(
            username="ordinarycustomer",
            password="SecureTestPassword123!",
        )

        self.client.force_login(customer)

        response = self.client.get(
            reverse("staff_dashboard")
        )

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("staff_dashboard")}',
            fetch_redirect_response=False,
        )

    def test_staff_dashboard_allows_staff_member(self):
        user_model = get_user_model()

        staff_user = user_model.objects.create_user(
            username="staffmember",
            password="SecureTestPassword123!",
            is_staff=True,
        )

        self.client.force_login(staff_user)

        response = self.client.get(
            reverse("staff_dashboard")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "accounts/staff_dashboard.html",
        )
        self.assertContains(response, "Staff Dashboard")

    def test_staff_dashboard_displays_all_requests(self):
        user_model = get_user_model()

        staff_user = user_model.objects.create_user(
            username="staffviewer",
            password="SecureTestPassword123!",
            is_staff=True,
        )

        customer = user_model.objects.create_user(
            username="assistancecustomer",
            password="SecureTestPassword123!",
        )

        assistance_request = AssistanceRequest.objects.create(
            customer=customer,
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Flat battery",
            location_type="roadside",
            location_description="Supermarket car park",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="Customer",
            contact_last_name="Test",
            contact_phone="07123456789",
        )

        self.client.force_login(staff_user)

        response = self.client.get(
            reverse("staff_dashboard")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            str(assistance_request.reference),
        )
        self.assertQuerySetEqual(
            response.context["assistance_requests"],
            [assistance_request],
        )

    def test_staff_dashboard_displays_request_details(self):
        user_model = get_user_model()

        staff_user = user_model.objects.create_user(
            username="detailsstaff",
            password="SecureTestPassword123!",
            is_staff=True,
        )

        AssistanceRequest.objects.create(
            vehicle_type="car",
            problem_type="breakdown",
            problem_description="Flat battery",
            location_type="roadside",
            location_description="Supermarket car park",
            occupant_count=1,
            assistance_needs="no",
            occupant_safety="yes",
            contact_first_name="John",
            contact_last_name="Smith",
            contact_phone="07123456789",
        )

        self.client.force_login(staff_user)

        response = self.client.get(reverse("staff_dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")
        self.assertContains(response, "Smith")
        self.assertContains(response, "07123456789")
        self.assertContains(response, "Car")
        self.assertContains(response, "Breakdown")
        self.assertContains(response, "Supermarket car park")


class EditAccountViewTests(TestCase):

    def test_edit_account_requires_login(self):
        response = self.client.get(reverse("edit_account"))

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("edit_account")}',
        )

    def test_logged_in_customer_can_view_account_details(self):
        user = get_user_model().objects.create_user(
            username="testcustomer",
            password="SecureTestPassword123!",
            first_name="John",
            last_name="Smith",
            email="john@example.com",
        )

        self.client.force_login(user)

        response = self.client.get(reverse("edit_account"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "accounts/edit_account.html",
        )

        form = response.context["form"]

        self.assertEqual(form.instance.pk, user.pk)
        self.assertEqual(form["first_name"].value(), "John")
        self.assertEqual(form["last_name"].value(), "Smith")
        self.assertEqual(form["email"].value(), "john@example.com")

    def test_customer_can_update_own_account_details(self):
        user = get_user_model().objects.create_user(
            username="testcustomer",
            password="SecureTestPassword123!",
            first_name="John",
            last_name="Smith",
            email="john@example.com",
        )

        self.client.force_login(user)

        response = self.client.post(
            reverse("edit_account"),
            {
                "first_name": "James",
                "last_name": "Jones",
                "email": "james@example.com",
            },
        )

        user.refresh_from_db()

        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(user.first_name, "James")
        self.assertEqual(user.last_name, "Jones")
        self.assertEqual(user.email, "james@example.com")

    def test_customer_cannot_modify_another_customers_account(self):
        user_model = get_user_model()

        customer_a = user_model.objects.create_user(
            username="customer_a",
            password="SecureTestPassword123!",
            first_name="John",
        )

        customer_b = user_model.objects.create_user(
            username="customer_b",
            password="SecureTestPassword123!",
            first_name="Sarah",
            email="sarah@example.com",
        )

        self.client.force_login(customer_a)

        response = self.client.post(
            reverse("edit_account"),
            {
                "first_name": "James",
                "last_name": "Jones",
                "email": "james@example.com",
                "id": customer_b.pk,
            },
        )

        customer_a.refresh_from_db()
        customer_b.refresh_from_db()

        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(customer_a.first_name, "James")
        self.assertEqual(customer_b.first_name, "Sarah")
        self.assertEqual(customer_b.email, "sarah@example.com")

    def test_customer_cannot_grant_themselves_staff_permissions(self):
        user = get_user_model().objects.create_user(
            username="ordinarycustomer",
            password="SecureTestPassword123!",
            first_name="John",
        )

        self.client.force_login(user)

        response = self.client.post(
            reverse("edit_account"),
            {
                "first_name": "James",
                "last_name": "Smith",
                "email": "james@example.com",
                "is_staff": True,
                "is_superuser": True,
                "is_active": False,
            },
        )

        user.refresh_from_db()

        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(user.first_name, "James")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_invalid_account_details_are_not_saved(self):
        user = get_user_model().objects.create_user(
            username="testcustomer",
            password="SecureTestPassword123!",
            first_name="John",
            last_name="Smith",
            email="john@example.com",
        )

        self.client.force_login(user)

        response = self.client.post(
            reverse("edit_account"),
            {
                "first_name": "James",
                "last_name": "Jones",
                "email": "not-an-email",
            },
        )

        user.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Smith")
        self.assertEqual(user.email, "john@example.com")
