from django.urls import path
from . import views

urlpatterns = [
    path("", views.nursery_view, name="nursery"),
    path("fableseed-view/<int:seed>/", views.fableseed_view, name="fableseed-view"),
    path("plant-fableseed", views.create_fableseed_view, name="plant-fableseed"),
    path("grow-fablebranch", views.create_fablebranch_view, name="grow-fablebranch"),
]