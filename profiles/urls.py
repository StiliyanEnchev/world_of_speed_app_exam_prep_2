from django.urls import path, include

from profiles.views import IndexPageView, ProfileCreateView, ProfileDetailsView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('profile/', include([
            path('create/', ProfileCreateView.as_view(), name='create-profile'),
            path('details/', ProfileDetailsView.as_view(), name='profile-details')]
        ))
]