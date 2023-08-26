from django import forms

from FruitipediaApp.account.models import AccountModel


class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name'}
        )
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name'}
        )
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    class Meta:
        model = AccountModel
        fields = ('first_name', 'last_name', 'email', 'password')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ('first_name', 'last_name', 'image', 'age')
