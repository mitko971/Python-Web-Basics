from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from FruitipediaApp.account.models import AccountModel
from FruitipediaApp.fruits.form import FruitForm, EditFruitForm, DeleteFruitForm
from FruitipediaApp.fruits.models import FruitModel


# Create your views here.

class FruitCreateView(CreateView):
    template_name = 'fruits/create-fruit.html'
    form_class = FruitForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AccountModel.objects.all()
        return context


class FruitDetailView(DetailView):
    template_name = 'fruits/details-fruit.html'
    model = FruitModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AccountModel.objects.all()
        return context


class FruitEditView(UpdateView):
    template_name = 'fruits/edit-fruit.html'
    form_class = EditFruitForm
    model = FruitModel
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AccountModel.objects.all()
        return context


class FruitDeleteView(DeleteView):
    template_name = 'fruits/delete-fruit.html'
    model = FruitModel
    form_class = DeleteFruitForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['profile'] = AccountModel.objects.all()
        return context
