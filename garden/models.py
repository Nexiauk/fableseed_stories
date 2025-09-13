"""
Models for the Fableseed application's user and garden system.

Defines models related to user profiles and the flowers they earn:

- UserFlower: Tracks flowers earned by users from seeds and branches.
- UserProfile: Stores extended profile information for each user,
  including display name, profile picture, bio, and fablebuds count.

Includes helper methods for string representations and image URLs.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from nursery.models import Fableseed, FableBranch, Flower


class UserFlower(models.Model):
    """
    Represents flowers earned by a user in the Fableseed ecosystem.

    Meta:
        ordering: Querysets order by flower.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    flower = models.ForeignKey(
        Flower,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(default=0)
    earned_from_seed = models.ForeignKey(
        Fableseed,
        on_delete=models.CASCADE
    )
    earned_from_branch = models.ForeignKey(
        FableBranch,
        on_delete=models.CASCADE,
        related_name="reward"
    )
    earned_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["flower"]

    def __str__(self):
        """
        Return a human-readable string for the UserFlower instance.
        Pluralises the flower name if quantity > 1.
        """
        if self.quantity == 1:
            return f"{self.quantity} {self.flower} earned"
        else:
            return f"{self.quantity} {self.flower}s earned"

    def user_flower_image_url(self):
        """
        Returns the URL of the associated flower's image.
        """
        return self.flower.flower_image.url


class UserProfile(models.Model):
    """
    Stores profile information for a user in the Fableseed app.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    display_name = models.CharField(max_length=70)
    profile_picture = CloudinaryField(
        "image",
        default="placeholder_l62d5p"
    )
    bio = models.TextField()
    fablebuds_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the user profile.
        Uses display_name if available, otherwise falls back to the username.
        """
        return self.display_name if self.display_name else self.user.username

    def user_profile_image_url(self):
        """
        Returns the URL of the user's profile picture.
        """
        return self.profile_picture.url

    @property
    def get_display_name(self):
        """
        Provides the display name of the user.
        If the UserProfile does not exist, returns the username.
        """
        try:
            return self.userprofile.display_name
        except UserProfile.DoesNotExist:
            return self.username


User.add_to_class(
        'get_display_name',
        UserProfile.get_display_name
    )
