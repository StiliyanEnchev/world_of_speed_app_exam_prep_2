from django.core.exceptions import ValidationError
from django.utils.text import slugify

def username_validator(value):
    if value.lower() != slugify(value).replace('-', '_'):
        raise ValidationError("Username must contain only letters, digits, and underscores!")


