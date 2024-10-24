from django import forms

from profiles.models import Profile

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password'})}

class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']