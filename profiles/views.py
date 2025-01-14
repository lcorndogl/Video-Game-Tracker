from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view_profiles(request):
    """
    Renders the profiles page
    Shows users who have their visibility matching to the users logged in status
    """
    return render(
        request,
        "profiles/profiles.html",
    )

def manage_profile(request):
    """
    Renders the profiles page
    Shows users who have their visibility matching to the users logged in status
    """
    return render(
        request,
        "profiles/manage.html",
    )

def home(request):
    """
    Renders the profiles page
    Shows users who have their visibility matching to the users logged in status
    """
    return render(
        request,
        "profiles/index.html",
    )
