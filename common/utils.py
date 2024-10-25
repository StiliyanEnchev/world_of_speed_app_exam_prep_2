from cars.models import Car
from profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_cars():
    return Car.objects.all()

