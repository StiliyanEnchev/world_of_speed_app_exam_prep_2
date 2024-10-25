from django.urls import path, include

from cars.views import CarCreateView, CatalogueView, CarDetails, CarEdit, CarDelete

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('<pk>/details/', CarDetails.as_view(), name='car-details'),
    path('<pk>/edit/', CarEdit.as_view(), name='car-edit'),
    path('<pk>/delete/', CarDelete.as_view(), name='car-delete'),

]