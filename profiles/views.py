from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import User_Profile, User_Library, User


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
            return User_Profile.objects.filter(privacy__in=["1", "3"]).order_by("-created_on")
        else:
            return User_Profile.objects.filter(privacy__lt="2").order_by("-created_on")

    context_object_name = 'profiles'
    template_name = "profiles/profiles.html"
    paginate_by = 4

# class ProfileDetail(generic.DetailView):


def profile_detailed(request, username):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    # queryset = User.objects.filter(username=username).values()
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(User_Profile, user=user)
    library = User_Library.objects.filter(user=user)
    backlog = library.filter(completed=False)
    completed = library.filter(completed=True)
    print('profile', profile)
    context = {
        "user_identified": user,
        "profile": profile,
        "library": library,
        "backlog": backlog,
        "completed": completed
    }

    return render(
        request,
        "profiles/profile_detailed.html",
        context
    )
