from django.contrib import admin
from .models import User, MemberOfCongress, Rating, Opinion


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'created_at')

@admin.register(MemberOfCongress)
class MOCAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'party', 'chamber')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
  list_display = ('rating', 'user', 'member', 'created_at')

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
  list_display = ('text', 'user', 'member')