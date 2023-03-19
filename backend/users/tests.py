from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import registration_view, logout_view, UserListAPIView, forgot_password, reset_password, \
    role_assignment_view
from .models import User


class UserTestCase(APITestCase):
    """
        Tests to verify the correct usage of the user models
    """

    def setUp(self):
        self.register = {"email": "test@test.com", "first_name": "First", "last_name": "Last", "password": "Pass"}
        self.login = {"username": "test@test.com", "password": "Pass"}
        self.user = User.objects.create(username="user", email="user@mail.com")
        self.su = User.objects.create(role="SU", username="su")

    def testUserRegistration(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        response = registration_view(request).data
        self.assertEqual(response["email"], "test@test.com")
        self.assertIn("token", response)

    def testUserRegistrationMissingEmail(self):
        factory = APIRequestFactory()
        del self.register["email"]
        request = factory.post("/api/register/", self.register)
        response = registration_view(request).data
        self.assertEqual(response["email"][0], "This field is required.")
        self.assertNotIn("token", response)

    def testUserLogin(self):
        factory = APIRequestFactory()
        request = factory.post("/api/register/", self.register)
        registration_view(request)

        # Login to the newly made account
        request = factory.post("/api/login/", self.login)
        response = obtain_auth_token(request).data
        self.assertIn("token", response)

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
        self.assertEqual(response["message"], "Dit email adres bestaat niet.")

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
        request = factory.post("/api/reset/", {"email": "test@test.com", "otp": otp, "new_password": ""})
        response = reset_password(request).data
        self.assertIn("errors", response)

        # Test if we can reset password
        otp = User.objects.get(email="test@test.com").otp
        request = factory.post("/api/reset/", {"email": "test@test.com", "otp": otp, "new_password": "Pass"})
        response = reset_password(request).data
        self.assertEqual(response["message"], "New password is created")

    def testUserLogout(self):
        factory = APIRequestFactory()
        request = factory.get("/api/logout")
        force_authenticate(request, user=self.user)
        response = logout_view(request).data
        self.assertEqual(response, "User Logged out successfully")

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
