from django.db import models
from django.contrib.auth.models import User
from garden.models import UserProfile
from cloudinary.models import CloudinaryField
from django.utils.html import format_html

# Create your models here.
STATUS = ((0, "Pending"), (1, "Approved"))

class Fableseed(models.Model):
    """
    Represents a story seed created by a user, associated with a flower type.

    Attributes:
    Seed(Autofield): Primary key identifier for the seed.
    flower_type(ForeignKey): Reference to the associated flower object
    title(CharField): Title of the fable seed
    body(CharField): Story prompt written by the user
    approval_status(BooleanField): Indicates if the seed has been approved by admin. Default is false.
    created_on(DateTimeField): Timestamp when the seed was created
    edited_on(DateTimeField): Timestamp when the seed was last edited
    author(ForeignKey): Reference to the user who created the seed
    fablebuds_earnt(PositiveIntegerField): Number of fablebuds earned by the seed. Default is 1)

    Meta:
        ordering: Seeds are sorted by creation date descending (newest first)

    Methods:
        __str__: Returns a string representation of the seed including title and author
    """

    seed = models.AutoField(primary_key=True)
    flower_type = models.ForeignKey("nursery.Flower", on_delete=models.PROTECT)
    title = models.CharField(max_length=130)
    body = models.CharField(max_length=255)
    approval_status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fablebuds_earnt = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["-created_on"]
        

    def __str__(self):
        author_name = self.author.username if self.author else "Deleted User"
        return f"{self.title} by {author_name}"
    
    def title_trunc(self):
        return (
            f"{self.title[:17]}..."
            if len(self.title) > 17
            else f"{self.title}"
        )


class Flower(models.Model):
    """
    Represents flowers available in the database to associate with a fableseed.

    Attributes

        flower(AutoField): Primary key identifier for the flower.
        flower_name(CharField): The name of the flower.
        flower_image(CloudinaryField): An image representation of the flower for the user's garden and to populate on the fableseed.

    Meta:
        ordering: Flowers are sorted by flower name in ascending alphabetical order.

    Methods:
        __str__: Returns a string representation of the flower name.
    """

    flower = models.AutoField(primary_key=True)
    flower_name = models.CharField(max_length=255)
    flower_image = CloudinaryField("image", default="placeholder")

    class Meta:
        ordering = ["flower_name"]

    def __str__(self):
        return self.flower_name
    
    def flower_image_url(self):
        return format_html('<img src="{}" style="height: 50px; width: 50px;" />', self.flower_image.url)
    
class FableBranch(models.Model):
    """
    Represents a branching reply to the Fableseeds

    Attributes:
        branch(AutoField): Primary key identifier for the fablebranch.
        seed(ForeignKey): Links to the Fableseed that the branch replies to.
        body(TextField): Story content written by the user.
        created_on(DateTimeField): Timestamp when the branch was created.
        edited_on(DateTimeField): Timestamp when the branch was last edited.
        author(ForeignKey): Reference to the user who created the branch.
        fablebuds_cost(PositiveIntegerField): Number of fablebuds it costs the user to write/purchase the branch. Default is 1.

    Meta:
        sets verbose names for singular and plural versions of Fablebranch
    """

    branch = models.AutoField(primary_key=True)
    seed = models.ForeignKey("nursery.Fableseed", on_delete=models.PROTECT)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fablebuds_cost = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Fablebranch"
        verbose_name_plural = "Fablebranches"

    def __str__(self):
        """
        Returns a string representation of the fablebranch.

        If the story body is longer than 50 characters, the text is truncated and followed by an ellipsis.
        Includes the author's username or "Deleted user" if the author no longer exists.
        """
        try:
            display_name = self.author.userprofile.display_name 
            
        except(AttributeError, UserProfile.DoesNotExist):
            display_name =  "Deleted User"
        return (
            f"{self.body[:50]}... by {display_name}"
            if len(self.body) > 50
            else f"{self.body} by {display_name}"
        )
