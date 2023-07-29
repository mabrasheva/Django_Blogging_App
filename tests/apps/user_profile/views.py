from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from django.urls import reverse

UserModel = get_user_model()


class BaseUserTestCase(TestCase):
    VALID_USER_DATA = {
        'username': 'maria_mihaleva',
        'first_name': 'Maria',
        'last_name': 'Miihaleva',
        'password': 'ASDqwe123!@#',
        'email': 'maria@mihaleva.com',
    }

    def setUp(self):
        self.client = Client()


class RegisterUserViewTests(BaseUserTestCase):
    def test_register_user__when_valid_data__expect_registration_success(self):
        # Arrange - Define the URL for the view and valid form data
        register_url = reverse('user_register')

        # Act - Simulate the form submission
        response = self.client.post(register_url, data=self.VALID_USER_DATA)

        # Assert - Check the response status code
        self.assertEqual(200, response.status_code)

        # Check if the user is created in the database using the custom BlogUser model
        created_user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.assertEqual(created_user.first_name, self.VALID_USER_DATA['first_name'])
        self.assertEqual(created_user.last_name, self.VALID_USER_DATA['last_name'])
        self.assertEqual(created_user.email, self.VALID_USER_DATA['email'])

        # Check if the user's password is set correctly (using check_password method to compare hashed passwords)
        self.assertTrue(created_user.check_password(self.VALID_USER_DATA['password']))

        # Additional checks to verify user properties
        self.assertFalse(created_user.is_superuser)
        self.assertTrue(created_user.is_active)
        self.assertFalse(created_user.is_staff)

        # Check if the user has been assigned an ID (primary key)
        self.assertIsNotNone(created_user.pk)


class LogoutUserViewTests(BaseUserTestCase):

    def test_logout_user__when_authenticated__expect_logout_success(self):
        # Arrange - Create a test user and log in
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(username=self.VALID_USER_DATA['email'], password=self.VALID_USER_DATA['password'])

        # Act - Simulate the logout
        logout_url = reverse('user_logout')
        response = self.client.get(logout_url)

        # Assert - Check the response status code and if the user is logged out
        self.assertEqual(302, response.status_code)
        self.assertFalse('_auth_user_id' in self.client.session)


class ListUsersViewTests(BaseUserTestCase):

    def test_list_users__when_authenticated__expect_success(self):
        # Arrange - Create a test user and log in
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(username=self.VALID_USER_DATA['email'], password=self.VALID_USER_DATA['password'])

        # Act - Simulate the request to the ListUsersView
        list_users_url = reverse('users_list')
        response = self.client.get(list_users_url)

        # Assert - Check the response status code
        self.assertEqual(302, response.status_code)
