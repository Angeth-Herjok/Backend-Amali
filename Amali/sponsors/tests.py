from django.test import TestCase
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber
from .models import CustomUser

User = get_user_model()

class CustomUserModelTestCase(TestCase):
    def test_create_user_with_data(self):
        user_data = {
            'username': 'AmaliTeam',
            'email': 'angethherjok@gmail.com',
            'phoneNumber': PhoneNumber.from_string('+254750002644', region='KE'),
            'organisation': 'sport',
            'bio': 'wwee',
        }

        user = CustomUser.objects.create_user(**user_data)

     
        self.assertEqual(user.username, 'AmaliTeam')
        self.assertEqual(user.email, 'angethherjok@gmail.com')
        self.assertEqual(str(user.phoneNumber), '+254750002644')
        self.assertEqual(user.organisation, 'sport')
        self.assertEqual(user.bio, 'wwee')


   