from django.shortcuts import render
from django.views.generic import ListView

from FruitipediaApp.account.models import AccountModel
from FruitipediaApp.fruits.models import FruitModel


# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = AccountModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = AccountModel.objects.all()
        return context


class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = FruitModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = FruitModel.objects.all()

        return context
