from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fableseed(models.Model):
    seed = models.AutoField()
    flower_type = models.ForeignKey('Flower', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    approval_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    fablebuds_earnt = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title