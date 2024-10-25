from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from common.utils import get_profile
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


class IndexPageView(TemplateView):
    template_name = 'index.html'


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('home')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile-details.html'
    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sum = sum(car.price for car in get_profile().cars.all())

        context['total_sum'] = total_sum
        context['items'] = Profile.objects.all()  # Fetch all items from YourModel

        return context