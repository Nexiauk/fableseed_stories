"""
Admin configuration for the Garden app.

Registers and customizes the Django admin interface for:
- UserFlower: Displays flowers earned by users, with custom columns for
  flower image and associated Fableseed title.
- UserProfile: Managed inline within the User admin.
- User: Uses a custom UserAdmin to include the UserProfile inline and
  customise list display.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserFlower, UserProfile


# Register your models here.
@admin.register(UserFlower)
class UserFlowerAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the UserFlower model.
    Provides custom list display for user, flower, quantity, earned date,
    flower image, and associated Fableseed.
    """
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
    """
    Inline admin configuration for the UserProfile model.
    Used within the User admin interface to display and edit profiles.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.
    Includes the UserProfile inline and custom list display.
    """
    inlines = (UserProfileInline,)
    list_display = [
        "userprofile__display_name",
        "username",
        "email",
        "is_staff",
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
