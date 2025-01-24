from django import forms
from .models import Comment, User_Profile, User_Library, Privacy


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class FavouritesForm(forms.ModelForm):
    privacy = forms.ModelChoiceField(
        queryset=Privacy.objects.all(), empty_label=None)

    class Meta:
        model = User_Profile
        fields = ('game', 'platform', 'privacy')

