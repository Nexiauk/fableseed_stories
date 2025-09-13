from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from nursery.models import Fableseed, FableBranch, Flower


class UserFlower(models.Model):
    """
    Represents flowers earned by a user in the Fableseed ecosystem.

    Attributes:
        user (ForeignKey): Reference to the user who earned the flowers.
        flower (ForeignKey): Reference to the type of flower earned.
        quantity (PositiveIntegerField): Number of flowers earned.
        earned_from_seed (ForeignKey): Seed that generated the flowers.
        earned_from_branch (ForeignKey): Branch that generated the flowers.
        earned_on (DateTimeField): Timestamp when the flowers were earned.

    Meta:
        ordering: Querysets order by flower.

    Methods:
        __str__: Returns a string describing the flowers earned.
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

    Attributes:
        user (OneToOneField): Links to the Django User.
        display_name (CharField): Name shown publicly for the user.
        profile_picture (CloudinaryField): Profile image stored in Cloudinary.
        bio (TextField): User's biography.
        fablebuds_count (PositiveIntegerField): Fablebuds quantity.

    Methods:
        __str__: if the user has a display name, it will return that.
        If not, it will default to their username.
        user_profile_image_url: Custom method for image url.
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
