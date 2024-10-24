from django import forms

from cars.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']


class CarCreateForm(BaseCarForm):
    pass


class CarEditForm(BaseCarForm):
    pass


class CarDeleteForm(BaseCarForm):
    pass
