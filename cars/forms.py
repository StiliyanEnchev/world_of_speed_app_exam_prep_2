from django import forms

from cars.models import Car
from common.mixins import ReadOnlyMixin


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }



class CarCreateForm(BaseCarForm):
    pass


class CarEditForm(BaseCarForm):
    pass


class CarDeleteForm(ReadOnlyMixin, BaseCarForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price']
