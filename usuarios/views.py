from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.views.generic import CreateView, UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user:
            login(self.request, user)
        return response

class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    def get_success_url(self):
        # Redirige al usuario a la página de inicio después de iniciar sesión
        return reverse_lazy('inicio')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('inicio')

class ProfileView(DetailView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user
    