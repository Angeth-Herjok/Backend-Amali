from django.test import TestCase
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber

CustomUser = get_user_model()

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'AmaliTeam',
            'email': 'angethherjok@gmail.com',
            'phoneNumber': '+254750002644',
            'organisation': 'sport',
            'bio': 'wwee'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_custom_user_creation(self):
        self.assertTrue(isinstance(self.user, CustomUser))
        self.assertEqual(str(self.user), 'AmaliTeam')

    def test_phone_number_field(self):
        self.assertTrue(isinstance(self.user.phoneNumber, PhoneNumber))
        self.assertEqual(self.user.phoneNumber.as_e164, '+254750002644')

    def test_user_fields(self):
        self.assertEqual(self.user.username, 'AmaliTeam')
        self.assertEqual(self.user.email, 'angethherjok@gmail.com')
        self.assertEqual(self.user.organisation, 'sport')
        self.assertEqual(self.user.bio, 'wwee')

    def test_unique_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(**self.user_data)

    def test_user_defaults(self):
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.is_active)

    def test_user_full_name(self):
        full_name = 'AmaliTeam'
        self.assertEqual(self.user.get_full_name(), full_name)

    def test_user_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'AmaliTeam')
