from django import forms
from .models import Comment, User_Profile, User_Library


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class FavouritesForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('game', 'platform', 'privacy')