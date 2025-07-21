from django.contrib import admin
from .models import UserFlower

# Register your models here.
@admin.register(UserFlower)
class UserFlowerAdmin(admin.ModelAdmin):
    list_display = ["user", "flower", "quantity", "earned_on", "user_flower_image", "user_fableseed",]


    def user_flower_image(self, obj):
        return obj.flower.flower_image.url
    
    def user_fableseed(self, obj):
        return obj.earned_from_seed.title