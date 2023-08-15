from django.core.exceptions import ValidationError


def validate_name(value):
    if not value[0].isapha():
        raise ValidationError("Your name must start with a letter!")