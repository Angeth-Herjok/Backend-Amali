from django.db import models
from django.contrib import admin

# Create your views here

class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def register_user(self):
        self.save()

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    def is_exist(self):
        return Signup.objects.filter(email=self.email).exists()

    class Meta:
        verbose_name_plural = "Signups"

class Login(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def register_user(self):
        self.save()

    @classmethod
    def get_user_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

    def is_exist(self):
        return Login.objects.filter(email=self.email).exists()

    class Meta:
        verbose_name_plural = "Logins"
