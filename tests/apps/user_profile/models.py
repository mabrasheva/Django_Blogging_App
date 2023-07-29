from django.core.exceptions import ValidationError
from django.test import TestCase

from django_blogging_app.apps.user_profile.models import BlogUser


class BlogUserTests(TestCase):
    VALID_USER_DATA = {
        'username': 'maria_mihaleva',
        'first_name': 'Maria',
        'last_name': 'Miihaleva',
        'password': 'ASDqwe123!@#',
        'email': 'maria@mihaleva.com',
    }
    FULL_NAME = f"{VALID_USER_DATA['first_name']} {VALID_USER_DATA['last_name']}"

    def _create_user(self, data, **kwargs):
        user_data = {
            **data,
            **kwargs,
        }

        return BlogUser(**user_data)

    def test_create__when_valid__expect_to_be_created(self):
        user = self._create_user(self.VALID_USER_DATA)
        user.full_clean()
        user.save()

        self.assertIsNotNone(user.pk)

    def test_create__when_first_name_has_1_more_than_valid_characters__expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, first_name='a' * BlogUser.FIRST_NAME_MAX_LEN + 'a')

        with self.assertRaises(ValidationError) as context:
            user.full_clean()

        exception = context.exception
        self.assertIn('Ensure this value has at most', str(exception))

    def test_create__when_last_name_has_1_more_than_valid_characters__expect_to_raise(self):
        user = self._create_user(self.VALID_USER_DATA, last_name='a' * BlogUser.LAST_NAME_MAX_LEN + 'a')

        with self.assertRaises(ValidationError) as context:
            user.full_clean()

        exception = context.exception
        self.assertIn('Ensure this value has at most', str(exception))

    def test_create__when_email_is_not_unique__expect_to_raise(self):
        user1 = self._create_user(self.VALID_USER_DATA)
        user1.full_clean()
        user1.save()

        # Create another user with the same email
        user2 = self._create_user(self.VALID_USER_DATA)

        with self.assertRaises(ValidationError) as context:
            user2.full_clean()

        exception = context.exception
        self.assertIn('User with this Email already exists.', str(exception))

    def test_full_name__when_both_first_name_and_last_name_exist__expect_full_name(self):
        user = self._create_user(self.VALID_USER_DATA)

        self.assertEqual(user.full_name, self.FULL_NAME)
