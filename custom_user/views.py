from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy
from . import models, forms
from .forms import LoginForm


class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    success_url = 'login/'
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:user-list')

class UserList(ListView):
    template_name = 'users/user_list.html'
    queryset = models.CustomUser.objects.all()

    def get_queryset(self):
        return models.CustomUser.objects.all()

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('users:user-list')