from django.urls import path

from FruitipediaApp.account.views import CreateProfile, DetailsProfile, EditProfile, DeleteProfile

urlpatterns = (
    path('create/', CreateProfile.as_view(), name='create profile'),
    path('details/', DetailsProfile.as_view(), name='details profile'),
    path('edit/', EditProfile.as_view(), name='edit profile'),
    path('delete/', DeleteProfile.as_view(), name='delete profile'),
)