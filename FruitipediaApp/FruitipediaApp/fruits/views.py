from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from FruitipediaApp.fruits.form import FruitForm
from FruitipediaApp.fruits.models import FruitModel


# Create your views here.

class FruitCreateView(CreateView):
    template_name = 'fruits/create-fruit.html'
    form_class = FruitForm
    success_url = reverse_lazy('dashboard')


class FruitDetailView(DetailView):
    template_name = 'fruits/details-fruit.html'
    model = FruitModel


class FruitEditView(UpdateView):
    pass


class FruitDeleteView(DeleteView):
    pass
