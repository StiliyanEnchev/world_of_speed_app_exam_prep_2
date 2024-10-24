from django import forms

from cars.models import Car


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


class CarDeleteForm(BaseCarForm):
    pass
