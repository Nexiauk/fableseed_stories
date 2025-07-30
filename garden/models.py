from django.db import models
from nursery.models import Fableseed, FableBranch, Flower

# Create your models here.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserFlower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    earned_from_seed = models.ForeignKey(Fableseed, on_delete=models.PROTECT)
    earned_from_branch = models.ForeignKey(FableBranch, on_delete=models.PROTECT)
    earned_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["flower"]

    def __str__(self):
        if self.quantity == 1:
            return f"{self.quantity} {self.flower} earned"
        else:
            return f"{self.quantity} {self.flower}s earned"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=70)
    profile_picture = CloudinaryField("image", default="placeholder")
    bio = models.TextField()
    fablebuds_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.display_name if self.display_name else self.user.username
