from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id','name','father_name','mobile_number', 'address']


UserAdmin.fieldsets +=(
    (
        'Custom fields', {
            'fields':('name','mobile_number','father_name','address')
        }
    ),
)