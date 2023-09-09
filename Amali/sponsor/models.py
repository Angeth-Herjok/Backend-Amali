from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = PhoneNumberField(default='')
    sponsor_ID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    organisation = models.CharField(max_length=255)
    bio = models.TextField()
    sponsorship_start_date = models.DateField()
    sponsorship_end_date = models.DateField()
    


    class Meta:
        verbose_name_plural="Sponsor"
