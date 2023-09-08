from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField


# Create your views here

class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def register_user(self):
        self.save()

    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    def is_exist(self):
        return Signup.objects.filter(email=self.email).exists()

    class Meta:
        verbose_name_plural = "Signups"


