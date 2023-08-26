from django.core.exceptions import ValidationError


def only_letters_in_fruit_name(value):
    for v in value:
        if not v.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
