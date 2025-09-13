"""
URL configuration for the static pages in the Fableseed project.

Includes routes for:
- Home page
- About page

Each URL pattern maps to the corresponding view function.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about")
]
