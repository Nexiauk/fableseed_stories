from django.urls import path
from . import views

urlpatterns = [
    path("", views.fableseed_view, name="nursery")
]