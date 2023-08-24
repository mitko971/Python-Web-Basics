from django.urls import path

from FruitipediaApp.common.views import IndexView, DashboardView

urlpatterns = (
    path('', IndexView.as_view(), name='home page'),
    path('dashboard', DashboardView.as_view(), name='dashboard')
)
