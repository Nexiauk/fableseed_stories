from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Fableseed(models.Model):
    seed = models.AutoField(primary_key=True)
    flower_type = models.ForeignKey('nursery.Flower', on_delete=models.PROTECT)
    title = models.CharField(max_length=130)
    body = models.CharField(max_length=255)
    approval_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    fablebuds_earnt = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
    

class Flower(models.Model):
    flower = models.AutoField(primary_key=True)
    flower_name = models.CharField(max_length=255)
    flower_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["flower_name"]

    def __str__(self):
        return self.flower_name
    
    class FableBranch(models.Model):
        seed_id = models.ForeignKey("nursery.Fableseed", on_delete=models.PROTECT)
        body = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)
        edited_on = models.DateTimeField(auto_now=True)
        author_id = models.ForeignKey(User, on_delete=models.PROTECT)
        fablebuds_cost = models.PositiveIntegerField(default=1)

        def __str__(self):
            return self.body
    