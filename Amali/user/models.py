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


    

