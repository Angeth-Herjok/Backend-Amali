from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# class Donation(models.Model):
#     full_name = models.CharField(max_length=255)  
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     email = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sponsored_donations')
#     phone_number = PhoneNumberField()

#     def __str__(self):
#         return f"Donation of {self.amount} from {self.full_name} to {self.email} for athlete {self.email.athlete}"

#     class Meta:
#         verbose_name_plural = "Donations"



class Donation(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def save(self, *args, **kwargs):
        if self.payment_confirmed():
            self.status = self.CONFIRMED
        else:
            self.status = self.PENDING

        super().save(*args, **kwargs)

    def payment_confirmed(self):
        return self.amount > 0 and self.status  
