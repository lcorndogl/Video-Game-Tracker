from django.contrib import admin
from .models import Favourite, Game, Platform
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Favourite)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('user', 'platform', 'game', 'created_on', 'updated_on')


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    list_display = ('game',)


@admin.register(Platform)
class PlatformAdmin(SummernoteModelAdmin):
    list_display = ('platform',)

# Register your models here.
