from django.contrib import admin
from django.contrib import admin
from .models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phoneNumber','sponsor_ID', 'organisation', 'bio','sponsorship_start_date','sponsorship_end_date') 
admin.site.register(Sponsor, SponsorAdmin)

