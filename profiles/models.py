from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import username_validator


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(
                limit_value=3,
                message="Username must be at least 3 chars long!"),
            username_validator,
        ])

    email = models.EmailField()

    age = models.IntegerField(
        MinValueValidator(21),
        help_text='Age requirement: 21 years and above.',
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
