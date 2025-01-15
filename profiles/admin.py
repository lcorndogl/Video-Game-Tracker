from django.contrib import admin
from .models import Favourite
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Favourite)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('user', 'platform', 'game', 'created_on', 'updated_on')

# Register your models here.
