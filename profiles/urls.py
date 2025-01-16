from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProfileList.as_view(), name='home'),
    path('', views.home, name='home'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('profiles/manage/', views.manage_profile, name='manage'),
]