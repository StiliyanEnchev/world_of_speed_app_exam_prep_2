from django.urls import path

from cars.views import CarCreateView

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='create-car'),
]