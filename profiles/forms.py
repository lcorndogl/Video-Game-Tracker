from django import forms
from .models import Comment, User_Profile, Privacy, User_Library, Game


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


class AddGameForm(forms.ModelForm):
    game = forms.ModelChoiceField(
        queryset=Game.objects.all(), empty_label=None)
    # completed = forms.ModelChoiceField(
    #     queryset=User_Library.objects.all(), empty_label=None)

    class Meta:
        model = User_Library
        fields = ('game', 'platform', 'completed')
