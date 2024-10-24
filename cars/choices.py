from django.db.models import TextChoices


class car_choices(TextChoices):
    RALLY = ('Rally', 'Rally')
    OPEN_WHEEL = ('Open-wheel', 'Open-wheel')
    KART = ('Kart', 'Kart')
    DRAG = ('Drag', 'Drag')
    OTHER = ('Other', 'Other')

