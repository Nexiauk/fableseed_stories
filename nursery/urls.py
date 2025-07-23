from django.urls import path
from . import views

urlpatterns = [
    path("", views.nursery_view, name="nursery")
]