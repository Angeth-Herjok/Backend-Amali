from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phoneNumber', 'organisation', 'bio')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('phoneNumber', 'organisation', 'bio'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.site_header = 'My Custom User Administration'
admin.site.site_title = 'Custom User Admin'
admin.site.index_title = 'Manage Custom Users'

