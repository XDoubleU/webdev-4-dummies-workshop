from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
  model = get_user_model
  list_display = [
    "email",
    "is_superuser"
  ]

admin.site.register(get_user_model(), CustomUserAdmin)