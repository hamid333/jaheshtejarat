from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def logout_view(request):
    logout(request)
    return redirect('home')
