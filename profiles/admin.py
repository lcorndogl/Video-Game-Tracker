from django.contrib import admin
from .models import User_Profile, Game, Platform, Privacy, User_Library, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(User_Profile)
class User_Profile(SummernoteModelAdmin):
    list_display = ('user', 'platform', 'game', 'created_on', 'updated_on',
                    'privacy')


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    list_display = ('game',)


@admin.register(Platform)
class PlatformAdmin(SummernoteModelAdmin):
    list_display = ('platform',)


@admin.register(Privacy)
class PrivacyAdmin(SummernoteModelAdmin):
    list_display = ("id", 'privacy')


@admin.register(User_Library)
class LibraryAdmin(SummernoteModelAdmin):
    list_display = ("id", 'game', 'user', 'created_on', 'updated_on',
                    'completed')


# Register your models here.
admin.site.register(Comment)
