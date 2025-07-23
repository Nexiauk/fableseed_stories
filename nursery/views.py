from django.shortcuts import render
from .models import Flower, Fableseed

# Create your views here.
def flower_view(request):
    flower_list = Flower.objects.all()
    context = {
        "flower_list": flower_list
    }
    page_url="nursery/nursery.html"
    return render(request, page_url, context)

def nursery_view(request):
    fableseed_list = Fableseed.objects.all()
    context = {
        "fableseed_list": fableseed_list
    }

    page_url = "nursery/nursery.html"
    return render(request, page_url, context)