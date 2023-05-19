from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import registration_view, logout_view, UserListAPIView, forgot_password, reset_password, \
    role_assignment_view, login_view
from .models import User
from ronde.models import LocatieEnum


class UserTestCase(APITestCase):
    """
        Tests to verify the correct usage of the user models
    """

    def setUp(self):
        self.loc1 = LocatieEnum.objects.create(name="Gent")
        self.loc2 = LocatieEnum.objects.create(name="Antwerpen")

        self.register = {"email": "test@test.com", "first_name": "First",
                         "last_name": "Last", "password": "Pass", "password2": "Pass", "phone_nr": "0",
                         "locations": [self.loc1.id, self.loc2.id]}
        #print(self.loc1)
        #print(self.loc2)
        #print(self.register)
        self.login = {"email": "test@test.com", "password": "Pass"}
        self.user = User.objects.create(username="user", email="user@mail.com")
        self.su = User.objects.create(role="SU", username="su")

    def testUserRegistration(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        response = registration_view(request).data

        self.assertEqual(response["email"], "test@test.com")
        self.assertIn("role", response)

    def testUserRegistrationMissingEmail(self):
        factory = APIRequestFactory()
        del self.register["email"]
        request = factory.post("/api/register/", self.register)
        response = registration_view(request).data

        self.assertTrue(len(response) > 0)
        self.assertEqual(response["errors"][0]["field"], ErrorDetail(
            string='email', code='invalid'))
        self.assertNotIn("token", response)

    def testUserLogin(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)

        registration_view(request)

        # Login to the newly made account
        request = factory.post("/api/login/", self.login)
        session = SessionMiddleware(login_view)
        response = session(request).data
        self.assertIn("role", response)

    def testUserForgotPassword(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        registration_view(request)

        # Test if email is sent for a valid email address
        request = factory.post("/api/forgot/", {"email": "test@test.com"})
        response = forgot_password(request).data
        self.assertEqual(response["message"], "Email is verstuurd")

        # Test if no email is sent if it does not exist in database
        request = factory.post("/api/forgot/", {"email": "test2@test.com"})
        response = forgot_password(request).data
        self.assertIn("errors", response)

    def testUserResetPassword(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        registration_view(request)

        # Make sure an error message is given when a non-existent email is entered
        request = factory.post("/api/reset/", {"email": "test2@test.com"})
        response = reset_password(request).data
        self.assertIn("errors", response)

        # Make sure an error message is given when OTP's don't match
        request = factory.post("/api/reset/", {"email": "test@test.com", "otp": ""})
        response = reset_password(request).data
        self.assertIn("errors", response)

        # Make sure new password isn't empty
        otp = User.objects.get(email="test@test.com").otp
        request = factory.post("/api/reset/", {"email": "test@test.com", "otp": otp, "password": ""})
        response = reset_password(request).data
        self.assertIn("errors", response)

        # Test if we can reset password
        otp = User.objects.get(email="test@test.com").otp
        request = factory.post("/api/reset/", {"email": "test@test.com", "otp": otp, "password": "Pass", "password2": "Pass"})
        response = reset_password(request).data
        self.assertEqual(response["message"], "New password is created")

    def testUserLogout(self):
        factory = APIRequestFactory()
        request = factory.post("/api/logout")
        force_authenticate(request, user=self.user)

        session = SessionMiddleware(logout_view)
        response = session(request).data
        self.assertEqual(response['message'], "You have been logged out succefully")

    def testListUserPermissions(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users")
        force_authenticate(request, user=self.user)
        response = UserListAPIView.as_view()(request).data

        # Normal user should not have permissions to view all users
        self.assertEqual(response["detail"].code, "permission_denied")

    def testUserRoleAssignment(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        registration_view(request)

        # Test permission for role assignment
        request = factory.post("/api/role/", {"role": "AD", "email": ""})
        force_authenticate(request, user=self.user)
        response = role_assignment_view(request).data
        self.assertEqual(response["detail"].code, "permission_denied")

        # Test if error is returned when email is empty
        request = factory.post("/api/role/", {"role": "AD", "email": ""})
        force_authenticate(request, user=self.su)
        response = role_assignment_view(request).data
        self.assertEqual(response["email"][0], "This field may not be blank.")

        # Make sure a superstudent can't promote a user to admin
        request = factory.post("/api/role/", {"role": "AD", "email": "test@test.com"})
        force_authenticate(request, user=self.su)
        response = role_assignment_view(request).data
        self.assertIn("errors", response)

        # Make sure a non-existent user cannot be promoted
        request = factory.post("/api/role/", {"role": "ST", "email": "test2@test.com"})
        force_authenticate(request, user=self.su)
        response = role_assignment_view(request).data
        self.assertIn("errors", response)

        # Make sure a non-existent user cannot be promoted
        request = factory.post("/api/role/", {"role": "ST", "email": "test@test.com"})
        force_authenticate(request, user=self.su)
        response = role_assignment_view(request).data
        self.assertEqual(response["message"], "test@test.com is nu een Student")
