from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fableseed(models.Model):
    seed = models.IntegerField()
    flower_type = models.ForeignKey(Flower, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    approval_status = models.BooleanField()
    created_on = models.DateTimeField()
    edited_on = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    fablebuds_earnt = models.PositiveIntegerField
