from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'created_at')

# Register your models here.
