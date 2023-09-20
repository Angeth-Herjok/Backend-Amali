from django.test import TestCase
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber
from .models import CustomUser

User = get_user_model()

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'AmaliTeam',
            'email': 'angethherjok@gmail.com',
            'phoneNumber': PhoneNumber.from_string('+254750002644', region='KE'),
            'organisation': 'sport',
            'bio': 'wwee',
        }

    def test_create_user_with_data(self):
        user = CustomUser.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            phoneNumber=self.user_data['phoneNumber'],
            organisation=self.user_data['organisation'],
            bio=self.user_data['bio'],
        )

        self.assertEqual(user.username, 'AmaliTeam')
        self.assertEqual(user.email, 'angethherjok@gmail.com')
        self.assertEqual(str(user.phoneNumber), '+254750002644')
        self.assertEqual(user.organisation, 'sport')
        self.assertEqual(user.bio, 'wwee')

    def test_create_superuser_with_data(self):
        admin_user = CustomUser.objects.create_superuser(
            username='AdminUser',
            email='admin@example.com',
            password='adminpassword',
            phoneNumber=self.user_data['phoneNumber'],
            organisation=self.user_data['organisation'],
            bio=self.user_data['bio'],
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_str_representation(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(str(user), 'AmaliTeam') 

    def test_user_is_active(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertTrue(user.is_active)

    def test_user_is_not_staff(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertFalse(user.is_staff)

    def test_user_is_not_superuser(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertFalse(user.is_superuser)
