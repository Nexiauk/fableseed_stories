"""
This module contains Django models for the Fableseed application.

Models:
- Fableseed: Story seeds created by users.
- Flower: Flowers associated with seeds.
- FableBranch: Branching replies to seeds.
"""
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Pending"), (1, "Approved"))


class Fableseed(models.Model):
    """
    Represents a story seed created by a user.

    Meta:
        ordering: Seeds are sorted by creation date descending.
    """

    seed = models.AutoField(primary_key=True)
    flower_type = models.ForeignKey(
        "nursery.Flower",
        on_delete=models.PROTECT
        )
    title = models.CharField(max_length=60)
    body = models.CharField(max_length=255)
    approval_status = models.IntegerField(
        choices=STATUS,
        default=0
        )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fablebuds_earnt = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        author_name = self.author.username if self.author else "Deleted User"
        return f"{self.title} by {author_name}"


class Flower(models.Model):
    """
    Flowers associated with a Fableseed.
    """

    flower = models.AutoField(primary_key=True)
    flower_name = models.CharField(max_length=255)
    flower_image = CloudinaryField("image", default="placeholder")
    fablebuds_cost = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["flower_name"]

    def __str__(self):
        return self.flower_name


class FableBranch(models.Model):
    """
    Represents a branching reply to the Fableseed.

    Meta:
        verbose_name: Singular name of the model.
        verbose_name_plural: Plural name of the model.
    """

    branch = models.AutoField(primary_key=True)
    seed = models.ForeignKey(
        "nursery.Fableseed",
        on_delete=models.PROTECT,
        related_name='fablebranches'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="fableauthor"
    )

    class Meta:
        verbose_name = "Fablebranch"
        verbose_name_plural = "Fablebranches"

    def __str__(self):
        """
        Return a string representation of the fablebranch.
        Truncates body to 50 characters if longer, appends author display name.
        """
        try:
            display_name = self.author.userprofile.display_name

        except (AttributeError, ObjectDoesNotExist):
            display_name = "Deleted User"
        return (
            f"{self.body[:50]}... by {display_name}"
            if len(self.body) > 50
            else f"{self.body} by {display_name}"
        )
