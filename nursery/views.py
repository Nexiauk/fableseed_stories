"""
Views for the Nursery app in the Fableseed project.

Provides functionality for:
- Displaying a paginated list of approved Fableseed objects (nursery view)
- Creating, viewing, and editing Fableseed and FableBranch objects
- Managing user interactions with Fableseed branches and flowers
- Deleting Fableseed or FableBranch objects with user feedback

All actions that modify content require the user to be logged in.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Fableseed, FableBranch
from garden.models import UserFlower
from .forms import (
    CreateFableseed,
    CreateFablebranch,
    EditFablebranch,
    EditFableseed
)


def nursery_view(request):
    """
    Display a paginated list of approved Fableseed objects in the nursery.
    Annotates each seed with its latest branch.
    """
    fableseed_list = Fableseed.objects.filter(approval_status=1)
    paginator = Paginator(fableseed_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    for seed in page_obj:
        latest_branch = (
            seed.fablebranches
            .all()
            .order_by("-created_on")
            .first()
        )
        seed.latest_branch = latest_branch
    context = {"page_obj": page_obj}
    page_url = "nursery/nursery.html"
    return render(request, page_url, context)


@login_required
def create_fableseed_view(request):
    """
    Allow a logged-in user to create a new Fableseed.
    Increments user's fablebuds_count and shows a success message if saved.
    """
    page_url = "nursery/cultivate.html"
    edit_type = "Fableseed"

    if request.method == "POST":
        form = CreateFableseed(request.POST)
        if form.is_valid():
            posted_seed = form.save(commit=False)
            posted_seed.author = request.user
            request.user.userprofile.fablebuds_count += 1
            request.user.userprofile.save()
            posted_seed.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your seed has been planted! "
                "The gardener will check it for you."
            )
            return redirect("fableseed-view", seed=posted_seed.pk)
        else:
            messages.add_message(
                request, messages.ERROR,
                "Error creating Fableseed"
            )
    else:
        form = CreateFableseed()
    return render(
        request,
        page_url,
        {"form": form, "edit_type": edit_type}
    )


def fableseed_view(request, seed):
    """
    Display a single Fableseed with its flower type and branches.
    """
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    flower = fableseed_post.flower_type
    branches_list = fableseed_post.fablebranches.all().order_by("created_on")
    can_grow = request.user.is_authenticated and fableseed_post.approval_status == 1
    context = {
        "fableseed": fableseed_post,
        "posted_branches": branches_list,
        "flower": flower,
        "can_grow": can_grow,
    }
    page_url = "nursery/fableseed-view.html"
    return render(request, page_url, context)


@login_required
def create_fablebranch_view(request, seed):
    """
    Allow a logged-in user to add a FableBranch to an existing Fableseed.
    Updates the user's garden with the corresponding flower.
    """
    fableseed_post = get_object_or_404(Fableseed, seed=seed)
    flower = fableseed_post.flower_type
    page_url = "nursery/cultivate.html"
    edit_type = "Fablebranch"

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
                    f"Your plant is growing!"
                    f"Your garden now contains a {flower}"
                )
            else:
                obj.quantity += 1
                obj.save()
                message_text = "Your plant is growing!"
            messages.success(
                request,
                message_text
            )
            return redirect("fableseed-view", seed=posted_branch.seed.pk)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error creating Fablebranch")
    else:
        form = CreateFablebranch()
    return render(
        request,
        page_url,
        {"form": form, "edit_type": edit_type}
    )


@login_required
def edit_fablebranch_view(request, branch_id):
    """
    Allow the author of a FableBranch to edit it.
    Displays messages based on success or failure.
    """
    fablebranch = get_object_or_404(
        FableBranch, pk=branch_id, author=request.user)
    page_url = "nursery/cultivate.html"
    edit_type = "Fablebranch"

    if request.method == "POST":
        edit_fablebranch_form = EditFablebranch(
            request.POST,
            instance=fablebranch
        )
        if edit_fablebranch_form.is_valid():
            edit_fablebranch_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your branch has been lovingly tended!"
            )
            return redirect(
                "fableseed-view",
                seed=fablebranch.seed.pk
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating Fablebranch"
            )
    else:
        edit_fablebranch_form = EditFablebranch(instance=fablebranch)
    return render(
        request, page_url,
        {"form": edit_fablebranch_form,
         "edit_type": edit_type}
    )


@login_required
def edit_fableseed_view(request, seed):
    """
    Allow the author of a Fableseed to edit it.
    Displays messages based on success or failure.
    """
    fableseed_post = get_object_or_404(
        Fableseed, seed=seed, author=request.user)
    page_url = "nursery/cultivate.html"
    edit_type = "Fableseed"

    if request.method == "POST":
        edit_fableseed_form = EditFableseed(
            request.POST,
            instance=fableseed_post
        )
        if edit_fableseed_form.is_valid():
            edit_fableseed_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your seed has been lovingly tended!"
            )
            return redirect("fableseed-view", seed=fableseed_post.pk)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating Fableseed"
            )
    else:
        edit_fableseed_form = EditFableseed(instance=fableseed_post)
    return render(
        request,
        page_url,
        {"form": edit_fableseed_form, "edit_type": edit_type}
    )


@login_required
def delete_view(request, type, id):
    """
    Delete a Fableseed or FableBranch authored by the user.
    Displays a success message after deletion.
    """
    if type == "seed":
        obj = get_object_or_404(Fableseed, pk=id, author=request.user)
        has_branches = obj.fablebranches.all()
        if has_branches:
            messages.error(
                request,
                "An established seed cannot be culled!"
            )
            return redirect("fableseed-view", seed=obj.pk)
    elif type == "branch":
        obj = get_object_or_404(FableBranch, pk=id, author=request.user)
        userflower = UserFlower.objects.get(user=request.user, flower=obj.seed.flower_type)
        if userflower:
            userflower.quantity -= 1
        if userflower.quantity <= 0:
            userflower.delete()
        else:
            userflower.save()
    else:
        messages.error(
            request,
            "Invalid object type!"
        )
        return redirect("nursery")
    obj.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        f"Your {type} has been pruned!"
    )

    return redirect("nursery")
