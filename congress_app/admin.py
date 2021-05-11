from django.contrib import admin
from .models import User, MemberOfCongress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'created_at')

@admin.register(MemberOfCongress)
class MOCAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'party', 'chamber')

# Register your models here.
