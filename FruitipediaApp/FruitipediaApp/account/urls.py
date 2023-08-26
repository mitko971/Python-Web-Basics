from django.urls import path

from FruitipediaApp.account.views import CreateProfile, DetailsProfile, edit_profile, delete_profile

urlpatterns = (
    path('create/', CreateProfile.as_view(), name='create profile'),
    path('details/', DetailsProfile.as_view(), name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
)