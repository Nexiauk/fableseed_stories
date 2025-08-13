from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

# Create your views here.
def garden_view(request, id):
    page_url = "garden/mygarden.html"
    user = get_object_or_404(User, pk=id)
    context = {"user":user,}
    return render(request, page_url, context)

@login_required
def edit_profile_view(request):
    page_url = "garden/edit-profile.html"
    if request.method == "POST" :
        user_form = EditProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.add_message(request, messages.SUCCESS, "Profile successfully updated")
            finished_url = reverse("mygarden", args=[request.user.pk])
            return redirect(finished_url)
        else:
            messages.add_message(request, messages.ERROR, "Error updating user profile")
    else:
        user_form = EditProfileForm(instance=request.user)
    return render(request, page_url, {"form":user_form})