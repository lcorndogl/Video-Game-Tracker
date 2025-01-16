from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import User_Profile

# Create your views here.
# def view_profiles(request):
#     """
#     Renders the profiles page
#     Shows users who have their visibility matching to the users logged in status
#     """
#     return render(
#         request,
#         "profiles/profiles.html",
#     )


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


class ProfileList(generic.ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User_Profile.objects.filter(privacy__lt="3")
        else:
            return User_Profile.objects.filter(privacy__lt="2")

    context_object_name = 'profiles'
    template_name = "profiles/profiles.html"
    paginate_by = 4
