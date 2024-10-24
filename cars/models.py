from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from cars.choices import car_choices
from cars.validators import year_validator
from profiles.models import Profile


# Create your models here.

class Car(models.Model):

    type = models.CharField(
        max_length=10,
        choices=car_choices)

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1)],
    )

    year = models.IntegerField(
        validators=[year_validator]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={'unique': "This image URL is already in use! Provide a new one."},
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='cars'
    )