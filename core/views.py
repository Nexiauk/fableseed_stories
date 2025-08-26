from django.shortcuts import render

# Create your views here.
def home_view(request):
    page_url = "index.html"
    return render(request, page_url)