from django.contrib import admin

from .models import Account

from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'date_joined', 'is_active')
    list_display_links = ('phone_number', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account, AccountAdmin)
