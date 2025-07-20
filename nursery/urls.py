from django.urls import path
from . import views

urlpatterns = [
    path("", views.flower_view, name="nursery")
]