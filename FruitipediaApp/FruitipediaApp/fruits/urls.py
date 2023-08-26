
from django.urls import path, include

from FruitipediaApp.fruits.views import FruitCreateView, FruitDetailView, FruitEditView, FruitDeleteView

urlpatterns = (
    path("create/", FruitCreateView.as_view(), name="create fruit"),
    path('<int:pk>/', include([
        path('details/', FruitDetailView.as_view(), name="detail fruit"),
        path('edit/', FruitEditView.as_view(), name="edit fruit"),
        path('delete/', FruitDeleteView.as_view(), name="delete fruit"),
    ]))
)