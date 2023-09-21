from django.contrib import admin
from .models import Donation

# Register your models here.

class DonationAdmin(admin.ModelAdmin):
    list_display = ('amount',)

admin.site.register(Donation, DonationAdmin)


