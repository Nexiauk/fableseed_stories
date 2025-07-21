from django.db import models
from .models import Fableseed, Fablebranch, Flowers

# Create your models here.
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserFlower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flowers, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    earned_from_seed = models.ForeignKey(Fableseed, on_delete=models.PROTECT)
    earned_from_branch = models.ForeignKey(Fablebranch, on_delete=models.PROTECT)
    earned_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    

    def __str__(self):
        if self.quantity == 1:
            return f"{self.quantity} {self.flower} earned"
        else:
            return f"{self.quantity} {self.flower}s earned"