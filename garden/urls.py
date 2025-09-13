"""
URL configuration for the Garden app.

Defines URL patterns for viewing the garden and editing user profiles.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "mygarden/<int:id>/",
        views.garden_view,
        name="mygarden"
        ),
    path("edit-profile/",
         views.edit_profile_view,
         name="edit-profile"
         )
]
