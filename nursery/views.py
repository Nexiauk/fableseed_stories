from django.shortcuts import render

# Create your views here.
def nursery(request):
    """
    Renders the nursery.html template, which shows a grid of all Fableseeds

    Args:
        request (HttpRequest): The HTTP request object sent by the browser

    Returns:
        HttpResponse:The rendered HTML response showing the nursery page
    """
    return render(
        request,
        "nursery/nursery.html",
    )
