from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class Sponsor(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    phoneNumber = PhoneNumberField(default='')
    Sponsor_ID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    Organisation = models.CharField(max_length=255)
    Bio = models.TextField()
    sponsorship_start_date = models.DateField()
    sponsorship_end_date = models.DateField()
    
    class Meta:
        verbose_name_plural="Sponsor"
