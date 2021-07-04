"""Customizing the administrator interface."""

# django
from django.contrib import admin

# models
from accounts.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    """Indicate the fields to display."""
    list_display = ("username", "is_staff")


admin.site.register(CustomUser, UserAdmin)
