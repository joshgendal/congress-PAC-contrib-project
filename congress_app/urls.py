from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('add-api-data-to-db', views.add_api_data),
    path('delete-all-members', views.deleteMemberData),
    path('members-contributions-table', views.members_contributions_table)
]
