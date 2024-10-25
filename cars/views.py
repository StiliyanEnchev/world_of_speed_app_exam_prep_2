from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from cars.forms import CarCreateForm, CarEditForm
from cars.models import Car
from common.utils import get_profile, get_cars


# Create your views here.
class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class CatalogueView(ListView):
    template_name = 'catalogue.html'
    queryset = get_cars()


class CarDetails(DetailView):
    model = Car
    template_name = 'car-details.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Car.objects.filter(pk=pk)


class CarEdit(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'car-edit.html'
    success_url = reverse_lazy('catalogue')
