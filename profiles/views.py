from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User_Profile, User_Library, User, Comment
from .forms import CommentForm


def manage_profile(request):
    """
    Renders the profiles page
    Shows users who have their visibility matching to the users logged in status
    """
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(User_Profile, request)
    library = User_Library.objects.filter(user=user)
    context = {
        "library": library,
        "profile": profile,

    }
    return render(
        request,
        "profiles/manage.html",
        context,
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
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
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

    return HttpResponseRedirect(reverse('profile_detailed', args=[comment.profile]))


def comment_delete(request, comment_id):
    """
    Delete an individual comment.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.commenter == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# def favourite_edit(request, slug, comment_id):
#     """
#     Display an individual comment for edit.

#     **Context**

#     ``post``
#         An instance of :model:`blog.Post`.
#     ``comment``
#         A single comment related to the post.
#     ``comment_form``
#         An instance of :form:`blog.CommentForm`.
#     """
#     if request.method == "POST":

#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comment = get_object_or_404(Comment, pk=comment_id)
#         comment_form = CommentForm(data=request.POST, instance=comment)

#         if comment_form.is_valid() and comment.author == request.user:
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.approved = False
#             comment.save()
#             messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
#         else:
#             messages.add_message(request, messages.ERROR,
#                                 'Error updating comment!')

#     return HttpResponseRedirect(reverse('post_detail', args=[slug]))
