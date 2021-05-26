from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_contributions_table),
    path('register', views.register),
    path('login', views.login),
    path('add-api-data-to-db', views.add_api_data),
    path('delete-all-members', views.deleteMemberData),
    path('rate-comment/<str:cid>', views.rate),
    path('add-rating', views.add_rating),
    path('dashboard', views.dashboard),
    path('change-chamber', views.change_chamber),
    path('change-party', views.change_party),
    path('edit-rating-opinion', views.modify_edit_opinion),
    path('edit-rating-opinion/<int:rating_id>', views.edit_rating_opinion),
    path('signout', views.signout),
    path('rate-feed', views.rate_feed),
    path('rating/delete/<str:member_cid>', views.delete_rating)
]
