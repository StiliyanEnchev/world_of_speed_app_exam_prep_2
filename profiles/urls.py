from django.urls import path

from profiles.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
]