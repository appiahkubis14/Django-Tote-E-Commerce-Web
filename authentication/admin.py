from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')
    list_display_links = ('email','first_name')
    list_filter = ('is_admin', 'is_staff', 'is_active', 'is_superadmin')
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    ordering = ('date_joined',)
    readonly_fields = ('date_joined', 'last_login','password','is_admin', 'is_staff', 'is_active', 'is_superadmin')

admin.site.register(Account,AccountAdmin)