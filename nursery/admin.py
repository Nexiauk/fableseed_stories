from django.contrib import admin
from .models import Flower, Fableseed, FableBranch

# Register your models here.

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ["flower_name", "flower_image"]

@admin.register(Fableseed)
class FableseedAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "author",
        "flower_type",
        "flower_image",
        "body",
        "approval_status",
    )
    readonly_fields = ("flower_image",)
    list_display = ("title", "author", "flower_name", "flower_image", "approval_status")

    def flower_name(self, obj):
        if obj.flower_type:
            return obj.flower_type
        
    def flower_image(self, obj):
        if obj.flower_type.flower_image:
            return obj.flower_type.flower_image



admin.site.register(FableBranch)