from django.contrib import admin
from .models import Flower, Fableseed, FableBranch

# Register your models here.

admin.site.register(Flower)
admin.site.register(Fableseed)
admin.site.register(FableBranch)