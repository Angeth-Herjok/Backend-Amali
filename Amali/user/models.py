# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=100)
#     phone_number = PhoneNumberField(unique=True, blank=True, null=True)
#     password = models.CharField(max_length=128)
#     confirm_password = models.CharField(max_length=128,null=True)
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )




from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('athlete', 'Athlete'),
        ('regular_user', 'Regular User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(_('Role'), max_length=15, choices=USER_ROLES, default='regular_user')
    email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, null=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email

# class Athlete(models.Model):
#     # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
#     # age = models.PositiveIntegerField()
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#     ]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')
#     # profile_picture = models.ImageField(upload_to='profile_pictures/')
#     # achievements = models.TextField()
#     password = models.CharField(max_length=128, null=True)
#     confirm_password = models.CharField(max_length=128, null=True)

#     def __str__(self):
#         return self.email


    

