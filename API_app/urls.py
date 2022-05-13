from django.urls import path
from .views import BlogCreateAPIView, ContactAPIView, firstAPI, registrationAPI

urlpatterns = [
    path('profile/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
    path('blog/', BlogCreateAPIView.as_view()),
]
