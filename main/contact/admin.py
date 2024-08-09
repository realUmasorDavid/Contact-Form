from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'message', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'message', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(contact, ContactAdmin)