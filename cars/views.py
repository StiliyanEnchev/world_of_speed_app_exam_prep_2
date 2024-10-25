from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
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


class CarDelete(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)