from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile, UserFlower

# Create your views here.
def garden_view(request, id):
    page_url = "garden/mygarden.html"
    user = get_object_or_404(User, pk=id)
    context = {"user":user,}
    return render(request, page_url, context)