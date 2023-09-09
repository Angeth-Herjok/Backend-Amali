from django.contrib import admin
from.models import Signup

# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "confirm_password", "phone_number", "email", "password")


admin.site.register(Signup, SignupAdmin)

