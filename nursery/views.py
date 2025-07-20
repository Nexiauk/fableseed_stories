from django.shortcuts import render
from .models import Flower

# Create your views here.
def nursery(request):
    """
    Renders the nursery.html template, which shows a grid of all Fableseeds

    Args:
        request (HttpRequest): The HTTP request object sent by the browser

    Returns:
        HttpResponse:The rendered HTML response showing the nursery page
    """
    return render(
        request,
        "nursery/nursery.html",
    )

def flower_view(request):
    flower_list = Flower.objects.all()
    context = {
        "flower_list": flower_list
    }
    page_url="nursery/nursery.html"
    return render(request, page_url, context)