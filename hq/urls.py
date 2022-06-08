from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('jobs/', JobsView.as_view(), name='job_listing'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutUsView.as_view(), name='about'),
]

