from django.urls import reverse_lazy
from django.views.generic import CreateView

from cars.forms import CarCreateForm
from cars.models import Car
from common.utils import get_profile


# Create your views here.
class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car-create.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)

