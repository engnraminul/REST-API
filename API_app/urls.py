from django.urls import path
from .views import firstAPI, registrationAPI

urlpatterns = [
    path('profile/', firstAPI),
    path('registration/', registrationAPI),
]
