from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view_profiles(request):

    return HttpResponse("Profiles Testing!")
