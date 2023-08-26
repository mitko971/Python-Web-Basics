from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from FruitipediaApp.account.forms import CreateProfileForm
from django.contrib.auth import views as auth_views

from FruitipediaApp.account.models import AccountModel


# Create your views here.


class CreateProfile(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard')


class DetailsProfile(auth_views.TemplateView):
    template_name = 'profile/details-profile.html'


class EditProfile(auth_views.FormView):
    template_name = 'profile/edit-profile.html'
    form_class = CreateProfileForm


class DeleteProfile(DeleteView):
    pass
