from django.contrib import admin
from .models import Flower, Fableseed, FableBranch

# Register your models here.

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ["flower_name", "flower_image"]

admin.site.register(Fableseed)
admin.site.register(FableBranch)