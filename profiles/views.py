from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from profiles.forms import ProfileCreateForm
from profiles.models import Profile


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile-create.html'
