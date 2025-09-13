"""
Admin configuration for the Fableseed app.

Registers models Flower, Fableseed, and FableBranch with the Django admin site.
Provides custom admin classes for Flower and Fableseed, including:
- Custom list displays and filters
- Image rendering for flowers
- Admin actions such as approving Fableseed posts
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Flower, Fableseed, FableBranch


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Flower model
    """
    list_display = ["flower_name", "flower_image_url", "fablebuds_cost"]
    list_filter = ("flower_name",)

    def flower_image_url(self, obj):
        """
        Returns HTML to display a 50x50 pixel image of the flower in the admin.
        """
        return format_html(
            '<img src="{}" style="height: 50px; width: 50px;" />',
            obj.flower_image.url
            )


@admin.action(description="Approve Fableseed")
def approve_fableseeds(modeladmin, request, queryset):
    """
    Admin action to approve selected Fableseed instances.

    Sets the approval_status of the selected Fableseed objects to 1.
    """
    queryset.update(approval_status=1)


@admin.register(Fableseed)
class FableseedAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Fableseed model.
    """
    fields = (
        "title",
        "author",
        "flower_type",
        "body",
        "approval_status",
    )
    list_display = (
        "title",
        "author",
        "flower_name",
        "body",
        "approval_status",
    )
    actions = [approve_fableseeds]
    list_filter = ("approval_status",)

    def flower_name(self, obj):
        """
        Returns the name of the flower type associated with this Fableseed.
        """
        if obj.flower_type:
            return obj.flower_type if obj.flower_type else None

    def flower_image(self, obj):
        """
        Returns the flower image associated with this Fableseed.
        """
        if obj.flower_type.flower_image:
            return obj.flower_type.flower_image


admin.site.register(FableBranch)
