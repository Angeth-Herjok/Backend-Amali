from django.contrib import admin
from django.db import models

# Create your models here.
class Donation(models.Model):
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    # athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
   
    def __str__(self):
        return f" Amount: {self.amount}"  
        # Donation from {self.sponsor.Name} to {self.athlete.name} 
      
    class Meta:
        verbose_name_plural= "Donations"

