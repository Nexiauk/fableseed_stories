from django.shortcuts import render, redirect
from .models import Flower, Fableseed
from .forms import CreateFableseed


# Create your views here.
def flower_view(request):
    flower_list = Flower.objects.all()
    context = {"flower_list": flower_list}
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)


def nursery_view(request):
    fableseed_list = Fableseed.objects.all()
    context = {"fableseed_list": fableseed_list}
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)


def fableseed_view(request, seed):
    fableseed_post = Fableseed.objects.get(seed=seed)
    context = {"fableseed": fableseed_post}
    page_url = "nursery/fableseed-view.html"
    return render(request, page_url, context)

def create_fableseed_view(request):
    page_url = "nursery/plant-fableseed.html"
    if request.method == "POST":
        create_fableseed=CreateFableseed(data=request.POST)
        if create_fableseed.is_valid():
            posted_seed=create_fableseed.save(commit=False)
            posted_seed.author=request.user
            posted_seed.save()    
        return redirect("fableseed-view", seed=posted_seed.pk)
    form = CreateFableseed()
    return render(request, page_url, {"form": form})
