from django.db import models
from nursery.models import Fableseed, FableBranch, Flower
from django.utils.html import format_html
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
    def user_profile_image(self):
        return format_html('<img src="{}" style="height: 150px; width: 150px;" />', self.profile_picture.url)
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user=instance)
        except Exception as e:
            print(f"Error creating profile for user {instance.id}: {e}")
