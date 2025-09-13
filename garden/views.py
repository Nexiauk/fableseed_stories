from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EditProfileForm
from .models import UserFlower

# Create your views here.


def garden_view(request, id):
    """
    Display the garden page for a specific user.

    Retrieves the user by ID and fetches all flowers the user has earned
    with quantity greater than zero. Renders the 'mygarden.html' template
    with the user and their flowers.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The primary key of the user whose garden is displayed.

    Returns:
        HttpResponse: Rendered garden page with user and flowers context.
    """
    page_url = "garden/mygarden.html"
    user = get_object_or_404(User, pk=id)
    user_flowers = UserFlower.objects.filter(user=user, quantity__gt=0)
    context = {"user": user, "user_flowers": user_flowers}
    return render(
        request,
        page_url,
        context
    )


@login_required
def edit_profile_view(request):
    """
    Allow the logged-in user to edit their profile.

    Handles both GET and POST requests:
    - GET: Renders the edit profile form pre-filled with current profile data.
    - POST: Validates the submitted form and updates the profile.
    Displays success or error messages using Django's messages framework.
    Redirects to the user's garden page on success.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered edit profile page with the form context.
    """
    page_url = "garden/edit-profile.html"
    profile = request.user.userprofile
    if request.method == "POST":
        user_form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if user_form.is_valid():
            user_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Profile successfully updated"
            )
            return redirect(
                "mygarden",
                request.user.pk
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating user profile"
            )
    else:
        user_form = EditProfileForm(instance=profile)
    return render(
        request,
        page_url,
        {"form": user_form}
    )
