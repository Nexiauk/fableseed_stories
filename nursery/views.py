from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Fableseed, FableBranch, Flower
from garden.models import UserFlower
from .forms import CreateFableseed, CreateFablebranch, EditFablebranch, EditFableseed


def nursery_view(request):
    fableseed_list = Fableseed.objects.filter(approval_status=1)
    paginator = Paginator(fableseed_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    for seed in page_obj:
        latest_branch = seed.fablebranches.all().order_by("-created_on").first()
        seed.latest_branch = latest_branch
    context = {"page_obj": page_obj}
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)


@login_required
def create_fableseed_view(request):
    page_url = "nursery/cultivate.html"
    if request.method == "POST":
        form = CreateFableseed(request.POST)
        if form.is_valid():
            posted_seed = form.save(commit=False)
            posted_seed.author = request.user
            request.user.userprofile.fablebuds_count += 1
            request.user.userprofile.save()
            posted_seed.save()
            messages.add_message(
                request, messages.SUCCESS, "Your seed has been planted!"
            )
            return redirect("fableseed-view", seed=posted_seed.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error creating Fableseed")
    else:
        form = CreateFableseed()
    return render(request, page_url, {"form": form})


def fableseed_view(request, seed):
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    flower = fableseed_post.flower_type
    branches_list = fableseed_post.fablebranches.all().order_by("created_on")
    context = {
        "fableseed": fableseed_post,
        "posted_branches": branches_list,
        "flower": flower,
    }
    page_url = "nursery/fableseed-view.html"
    return render(request, page_url, context)


@login_required
def create_fablebranch_view(request, seed):
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    flower = fableseed_post.flower_type
    page_url = "nursery/cultivate.html"
    if request.method == "POST":
        form = CreateFablebranch(request.POST)
        if form.is_valid():
            posted_branch = form.save(commit=False)
            posted_branch.seed = fableseed_post
            posted_branch.author = request.user
            posted_branch.save()
            obj, created = UserFlower.objects.get_or_create(
                user=request.user,
                flower=flower,
                defaults={
                    "earned_from_seed": fableseed_post,
                    "earned_from_branch": posted_branch,
                    "quantity": 1,
                },
            )
            if created:
                message_text = (
                    f"Your plant is growing! Your garden now contains a {flower}"
                )
            else:
                obj.quantity += 1
                obj.save()
                message_text = "Your plant is growing!"
            messages.success(request, message_text)
            return redirect("fableseed-view", seed=posted_branch.seed.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error creating Fablebranch")
    else:
        form = CreateFablebranch()
    return render(request, page_url, {"form": form})


@login_required
def edit_fablebranch_view(request, branch_id):
    fablebranch = get_object_or_404(FableBranch, pk=branch_id, author=request.user)
    page_url = "nursery/cultivate.html"
    edit_type = "Fablebranch"
    if request.method == "POST":
        edit_fablebranch_form = EditFablebranch(request.POST, instance=fablebranch)
        if edit_fablebranch_form.is_valid():
            edit_fablebranch_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your branch has been lovingly tended!"
            )
            return redirect("fableseed-view", seed=fablebranch.seed.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error updating Fablebranch")
    else:
        edit_fablebranch_form = EditFablebranch(instance=fablebranch)
    return render(request, page_url, {"form": edit_fablebranch_form, "edit_type":edit_type})


@login_required
def edit_fableseed_view(request, seed):
    fableseed_post = get_object_or_404(Fableseed, seed=seed, author=request.user)
    page_url = "nursery/cultivate.html"
    edit_type = "Fableseed"
    if request.method == "POST":
        edit_fableseed_form = EditFableseed(request.POST, instance=fableseed_post)
        if edit_fableseed_form.is_valid():
            edit_fableseed_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your seed has been lovingly tended!"
            )
            return redirect("fableseed-view", seed=fableseed_post.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error updating Fableseed")
    else:
        edit_fableseed_form = EditFableseed(instance=fableseed_post)
    return render(request, page_url, {"form": edit_fableseed_form, "edit_type":edit_type})

@login_required
def delete_fableseed_view(request, seed):
    fableseed_post = Fableseed.objects.get(seed=seed)
    if fableseed_post.author == request.user:
        fableseed_post.delete()
        messages.add_message(request, messages.SUCCESS, "Your seed has been pruned!")
        return redirect("nursery")
