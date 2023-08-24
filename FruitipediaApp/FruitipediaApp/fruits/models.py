from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruits.validators import only_letters_in_fruit_name


# Create your models here.

class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2, ),
            only_letters_in_fruit_name,
        ]

    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )