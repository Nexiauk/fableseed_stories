from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Fableseed
from .forms import CreateFableseed, CreateFablebranch


def nursery_view(request):
    fableseed_list = Fableseed.objects.all()
    paginator = Paginator(fableseed_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    for seed in page_obj:
        latest_branch = seed.fablebranches.all().order_by("-created_on").first()
        seed.latest_branch = latest_branch
    context = {"page_obj": page_obj}
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)


def create_fableseed_view(request):
    page_url = "nursery/plant-fableseed.html"
    if request.method == "POST":
        form = CreateFableseed(request.POST)
        if form.is_valid():
            posted_seed = form.save(commit=False)
            posted_seed.author = request.user
            posted_seed.save()
            return redirect("fableseed-view", seed=posted_seed.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error creating Fableseed")
    else:
        form = CreateFableseed()
    return render(request, page_url, {"form": form})


def fableseed_view(request, seed):
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    branches_list = fableseed_post.fablebranches.all().order_by("created_on")
    context = {"fableseed": fableseed_post, "posted_branches": branches_list}
    page_url = "nursery/fableseed-view.html"
    return render(request, page_url, context)


def create_fablebranch_view(request, seed):
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    page_url = "nursery/grow-fablebranch.html"
    if request.method == "POST":
        form = CreateFablebranch(request.POST)
        if form.is_valid():
            posted_branch = form.save(commit=False)
            posted_branch.seed = fableseed_post
            posted_branch.author = request.user
            posted_branch.save()
            posted_url = reverse("fableseed-view", args=[fableseed_post.pk])
            posted_url_with_branch_id = f"{posted_url}?branch={posted_branch.pk}"
            return redirect(posted_url_with_branch_id)
        else:
            messages.add_message(request, messages.ERROR, "Error creating Fablebranch")
    else:
        form = CreateFablebranch()
    return render(request, page_url, {"form": form})
