from django.urls import path, include

from profiles.views import IndexPageView, ProfileCreateView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('profile/', include([
            path('create/', ProfileCreateView.as_view(), name='create-profile')]
        ))
]