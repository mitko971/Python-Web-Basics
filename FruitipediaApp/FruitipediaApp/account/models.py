from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.account.validators import validate_name


# Create your models here.

class AccountModel(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            MinLengthValidator(2, ),
            validate_name,
        ),
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            MinLengthValidator(1, ),
            validate_name,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )
    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(8,),
        )
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )
