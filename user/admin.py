from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'last_login']
    list_editable = ['is_staff', 'is_superuser']

    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
