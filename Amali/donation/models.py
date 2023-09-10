
from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f" Amount: {self.amount}"  
       
    class Meta:
        verbose_name_plural = "Donation"        
