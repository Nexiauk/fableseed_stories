from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.nursery_view, name="nursery"),
    path("accounts/", include("allauth.urls")),
    path("fableseed-view/<int:seed>/", views.fableseed_view, name="fableseed-view"),
    path("plant-fableseed", views.create_fableseed_view, name="plant-fableseed"),
    path("grow-fablebranch/<int:seed>/", views.create_fablebranch_view, name="grow-fablebranch"),
    path("fablebranch/<int:branch_id>/edit/", views.edit_fablebranch_view, name="edit-fablebranch"),
    path("fableseed/<int:seed>/edit/", views.edit_fableseed_view, name="edit-fableseed"),
]