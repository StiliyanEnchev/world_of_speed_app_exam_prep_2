from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

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



