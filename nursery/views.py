from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Flower, Fableseed, FableBranch
from .forms import CreateFableseed, CreateFablebranch

def nursery_view(request):
    fableseed_list = Fableseed.objects.all()
    context = {"fableseed_list": fableseed_list}
    for seed in fableseed_list:
        latest = seed.fablebranches.all().order_by('-created_on').first()
        seed.latest_branch = latest
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)

def create_fableseed_view(request):
    page_url = "nursery/plant-fableseed.html"
    if request.method == "POST":
        create_fableseed=CreateFableseed(request.POST)
        if create_fableseed.is_valid():
            posted_seed=create_fableseed.save(commit=False)
            posted_seed.author=request.user
            posted_seed.save()    
        return redirect("fableseed-view", seed=posted_seed.pk)
    form = CreateFableseed()
    return render(request, page_url, {"form": form})

def fableseed_view(request, seed):
    fableseed_post = Fableseed.objects.get(seed=seed)
    branches_list = fableseed_post.fablebranches.all().order_by('created_on')
    context = {"fableseed": fableseed_post,
               "posted_branches": branches_list}
    page_url = "nursery/fableseed-view.html"
    return render(request, page_url, context)

def create_fablebranch_view(request, seed):
    fableseed_post = Fableseed.objects.get(seed=seed)
    page_url = "nursery/grow-fablebranch.html"
    if request.method == "POST":
        form=CreateFablebranch(request.POST)
        if form.is_valid():
            posted_branch=form.save(commit=False)
            posted_branch.seed = fableseed_post
            posted_branch.author=request.user
            posted_branch.save()    
            posted_url = reverse("fableseed-view", args=[fableseed_post.seed])
            posted_url_with_branch_id = f"{posted_url}?branch={posted_branch.pk}"
            return redirect(posted_url_with_branch_id)
    form = CreateFablebranch()
    return render(request, page_url, {"form": form})
