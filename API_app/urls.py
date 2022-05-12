from django.urls import path
from .views import ContactAPIView, firstAPI, registrationAPI

urlpatterns = [
    path('profile/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
]
