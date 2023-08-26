from django import forms

from FruitipediaApp.fruits.models import FruitModel


class FruitForm(forms.ModelForm):
    name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Fruit Name'}
        )
    )
    image = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Fruit Image URL'}
        )
    )
    description = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'placeholder': 'Fruit Description'}
        )
    )
    nutrition = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'placeholder': 'Nutrition Info'}
        )
    )

    class Meta:
        model = FruitModel
        fields = "__all__"
