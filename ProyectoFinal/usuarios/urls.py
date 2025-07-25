
from django.contrib import admin
from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, ProfileView

urlpatterns = [

path('register/', UserRegisterView.as_view() , name='register'),
path('login/', UserLoginView.as_view() , name='login'),
path('logout/', UserLogoutView.as_view(), name='logout'),
path('profile/', ProfileView.as_view(), name='profile'),
]

