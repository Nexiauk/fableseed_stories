from django.db import models
from django.utils.html import format_html
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
        earned_from_seed (ForeignKey): Reference to the Fableseed that generated the flowers.
        earned_from_branch (ForeignKey): Reference to the FableBranch that generated the flowers.
        earned_on (DateTimeField): Timestamp when the flowers were earned.

    Meta:
        ordering: Querysets order by flower.

    Methods:
        __str__: if the user has only earned one type of flower, it will return a string that 
        makes sense in the singular. Else it will return a string that makes sense with the plural.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    earned_from_seed = models.ForeignKey(Fableseed, on_delete=models.CASCADE)
    earned_from_branch = models.ForeignKey(
        FableBranch, on_delete=models.CASCADE, related_name="reward")
    earned_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["flower"]

    def __str__(self):
        if self.quantity == 1:
            return f"{self.quantity} {self.flower} earned"
        else:
            return f"{self.quantity} {self.flower}s earned"
        
    def user_flower_image_url(self):
        return self.flower.flower_image.url


class UserProfile(models.Model):
    """
    Stores profile information for a user in the Fableseed app.

    Attributes:
        user (OneToOneField): Links to the Django User.
        display_name (CharField): Name shown publicly for the user.
        profile_picture (CloudinaryField): User's profile image stored in Cloudinary.
        bio (TextField): User's biography.
        fablebuds_count (PositiveIntegerField): Number of fablebuds the user has.

    Methods:
        __str__: if the user has a display name, it will return that, if not, it will default to their username.
        user_profile_image: formats the url of the uploaded profile_picture into an image element with style applied.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='userprofile')
    display_name = models.CharField(max_length=70)
    profile_picture = CloudinaryField("image", default="placeholder_l62d5p")
    bio = models.TextField()
    fablebuds_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.display_name if self.display_name else self.user.username

    def user_profile_image_url(self):
        return self.profile_picture.url

    @property
    def get_display_name(self):
        try:
            return self.userprofile.display_name
        except UserProfile.DoesNotExist:
            return self.username
    User.add_to_class('get_display_name', get_display_name)
