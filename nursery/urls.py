from django.urls import path
from . import views

urlpatterns = [
    path("", views.nursery_view, name="nursery"),
    path("fableseed-view/<int:seed>/", views.fableseed_view, name="fableseed-view")
]