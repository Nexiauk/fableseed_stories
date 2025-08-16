from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserFlower
from .forms import EditProfileForm

# Create your views here.
def garden_view(request, id):
    page_url = "garden/mygarden.html"
    user = get_object_or_404(User, pk=id)
    user_flowers = UserFlower.objects.filter(user=user)
    context = {"user":user, "user_flowers": user_flowers}
    return render(request, page_url, context)

@login_required
def edit_profile_view(request):
    page_url = "garden/edit-profile.html"
    profile = request.user.userprofile
    if request.method == "POST" :
        user_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid():
            user_form.save()
            messages.add_message(request, messages.SUCCESS, "Profile successfully updated")
            return redirect("mygarden", request.user.pk)
        else:
            messages.add_message(request, messages.ERROR, "Error updating user profile")
    else:
        user_form = EditProfileForm(instance=profile)
    return render(request, page_url, {"form":user_form})