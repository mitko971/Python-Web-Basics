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


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = "__all__"


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
