from django.urls import path

from FruitipediaApp.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='home page'),
)
