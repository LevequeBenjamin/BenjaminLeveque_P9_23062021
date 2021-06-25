from django.contrib import admin

from accounts.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_staff")


admin.site.register(CustomUser, UserAdmin)
