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
        widgets = {
            'game': forms.Select(attrs={'id': 'fav_game_id'}),
            'platform': forms.Select(attrs={'id': 'fav_platform_id'}),
            'completed': forms.CheckboxInput(attrs={'id': 'fav_completed_id'}),
        }


class AddGameForm(forms.ModelForm):
    game = forms.ModelChoiceField(
        queryset=Game.objects.all(), empty_label=None)

    class Meta:
        model = User_Library
        fields = ('game', 'platform', 'completed')
        widgets = {
            'game': forms.Select(attrs={'id': 'add_game_id'}),
            'platform': forms.Select(attrs={'id': 'add_platform_id'}),
            'completed': forms.CheckboxInput(attrs={'id': 'add_completed_id'}),
        }
