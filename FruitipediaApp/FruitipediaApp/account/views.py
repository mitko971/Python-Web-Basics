from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from FruitipediaApp.account.forms import CreateProfileForm, EditProfileForm
from django.contrib.auth import views as auth_views

from FruitipediaApp.account.models import AccountModel
from FruitipediaApp.fruits.models import FruitModel


# Create your views here.


class CreateProfile(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard')


class DetailsProfile(auth_views.TemplateView):
    template_name = 'profile/details-profile.html'
    model = AccountModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AccountModel.objects.get()
        context['fruits'] = len(FruitModel.objects.all())
        return context


def edit_profile(request):
    user = AccountModel.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(initial=user.__dict__)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': AccountModel.objects.first()
    }
    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    user = AccountModel.objects.first()
    fruits = FruitModel.objects.all()

    if request.method == 'POST':
        user.delete()
        fruits.delete()
        return redirect('home page')
    context = {
        'profile': AccountModel.objects.first()
    }
    return render(request, 'profile/delete-profile.html', context=context)
