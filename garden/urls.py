from django.urls import path
from . import views

urlpatterns = [
    path("", views.garden_view, name="garden")
]