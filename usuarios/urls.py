
from django.contrib import admin
from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView

urlpatterns = [

path('register/', UserRegisterView.as_view() , name='register'),
path('login/', UserLoginView.as_view() , name='login'),
path('logout/', UserLogoutView.as_view(), name='logout'),
path('profile/', ProfileView.as_view(), name='profile'),
path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
path('avatar_update/', AvatarUpdateView.as_view(), name='avatar_update'),
path('about/', AvatarUpdateView.as_view(), name='about'),
]

