from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProfileList.as_view(), name='home'),
    path('', views.home, name='home'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('manage/profile/', views.manage_profile, name='manage'),
    path('profiles/<str:username>/', views.profile_detailed, name='profile_detailed'),
    path('profiles/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    # path('profile_view/', views.ProfileDetail.as_view(), name='profile_detailed'), 
]
