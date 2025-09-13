"""
Views for static pages in the Fableseed project.

Includes:
- Home page view
- About page view

Each view renders a corresponding template with no additional context.
"""

from django.shortcuts import render


def home_view(request):
    """
    Render the home page template for the project.
    """
    page_url = "index.html"
    return render(request, page_url)


def about_view(request):
    """
    Render the about page template for the project.
    """
    page_url = "about.html"
    return render(request, page_url)
