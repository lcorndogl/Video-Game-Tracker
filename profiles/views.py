from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User_Profile, User_Library, User, Comment, Privacy
from .forms import CommentForm, FavouritesForm, AddGameForm


def manage_profile(request):
    """
    Allows the user to modify their profile, including:
    Adding/removing games to their User_Library
    Updating their User_Profile
    Updating their User_Library game status'
    """
    user = get_object_or_404(User, username=request.user)
    # add if statement here to create User_Profile if it doesn't exist?
    if not User_Profile.objects.filter(user=user).exists():
        privacy = Privacy.objects.get(privacy="Private")
        User_Profile.objects.create(user=user, privacy=privacy)
    profile = get_object_or_404(User_Profile, user=user)
    library = User_Library.objects.filter(user=user)

    favourites_form = FavouritesForm(instance=profile)
    add_game_form = AddGameForm()

    if request.method == "POST":
        if 'favourites_form' in request.POST:
            favourites_form = FavouritesForm(data=request.POST,
                                             instance=profile)
            if favourites_form.is_valid():
                favourites_form.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Profile Updated!')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Error updating profile!')
        elif 'add_game_form' in request.POST:
            add_game_form = AddGameForm(data=request.POST)
            if add_game_form.is_valid():
                new_game = add_game_form.save(commit=False)
                new_game.user = user
                new_game.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Game added to library!')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Error adding game to library!')
        elif 'remove_game_id' in request.POST:
            game_id = request.POST.get('remove_game_id')
            entry = get_object_or_404(User_Library, id=game_id, user=user)
            entry.delete()
            messages.add_message(request, messages.SUCCESS,
                                 'Game removed from library!')
            return redirect('manage')
        elif 'update_library' in request.POST:
            for entry in library:
                entry_id = f'entry_{entry.id}'
                entry.completed = entry_id in request.POST
                entry.save()
            messages.add_message(request, messages.SUCCESS, 'Library updated!')
            return redirect('manage')

    context = {
        'profile': profile,
        'library': library,
        'favourites_form': favourites_form,
        'add_game_form': add_game_form,
    }
    return render(request, 'profiles/manage.html', context)


def home(request):
    """
    Displays the home page
    """
    return render(
        request,
        "profiles/index.html",
    )


class ProfileList(generic.ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return (
                User_Profile.objects
                .filter(privacy__in=["1", "3"])
                .order_by("-updated_on")
            )
        else:
            return (
                User_Profile.objects
                .filter(privacy__lt="2")
                .order_by("-updated_on")
            )

    context_object_name = 'profiles'
    template_name = "profiles/profiles.html"
    paginate_by = 6


def profile_detailed(request, username):
    """
    Display an individual :model:`User_Profile.User_Library`.
    **Context**
    ``User_Library``
        An instance of :model:`profiles.User_Library`.
    **Template:**
    :template:`profiles/profile_detailed.html`
    """

    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(User_Profile, user=user)
    library = User_Library.objects.filter(user=user)
    backlog = library.filter(completed=False)
    completed = library.filter(completed=True)

    comments = profile.comments.all().order_by("-created_on")
    comment_count = profile.comments.filter(approved=True).count()
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.profile = profile
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment Added!'
            )

    comment_form = CommentForm()

    print("About to render template")
    print('profile', profile)
    context = {
        "user_identified": user,
        "library": library,
        "backlog": backlog,
        "completed": completed,
        "profile": profile,
        "comment_form": comment_form,
        "comments": comments,
        "comment_count": comment_count,
    }

    return render(
        request,
        "profiles/profile_detailed.html",
        context,
    )


def comment_edit(request, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`profiles.User_Profile`.
    ``comment``
        A single comment related to the profile.
    ``comment_form``
        An instance of :form:`profiles.CommentForm`.
    """
    if request.method == "POST":

        user = get_object_or_404(User, username=request.user)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.commenter == request.user:
            comment = comment_form.save(commit=False)
            comment.commenter = user
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('profile_detailed',
                                        args=[comment.profile]))


def comment_delete(request, comment_id):
    """
    Delete an individual comment.

    **Context**
    ``profile``
        An instance of :model:`profiles.User_Profile`.
    ``comment``
        A single comment related to the profile.
    """

    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('profile_detailed',
                                        args=[comment.profile]))
