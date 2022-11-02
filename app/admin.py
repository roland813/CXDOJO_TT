from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import UserData


@admin.register(UserData)
class UsersAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "last_login", "date_joined"]
    search_fields = ["username"]
