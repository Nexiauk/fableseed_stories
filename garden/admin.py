from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import UserFlower, UserProfile


# Register your models here.
@admin.register(UserFlower)
class UserFlowerAdmin(admin.ModelAdmin):
    list_display = [
        "user", 
        "flower", 
        "quantity", 
        "earned_on", 
        "user_flower_image", 
        "user_fableseed",
        ]

    def user_flower_image(self, obj):
        return obj.flower.flower_image.url
    
    def user_fableseed(self, obj):
        return obj.earned_from_seed.title
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

    list_display = ("username", "profile_url", "profile_image_url",)

    def profile_url(self, obj):
        if obj.userprofile.profile_picture:
            return obj.userprofile.profile_picture  
    
    def profile_image_url(self, obj):
        return format_html('<img src="{}" style="height: 50px; width: 50px;" />', obj.userprofile.profile_picture.url)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)