from django.urls import path
from .views import firstAPI

urlpatterns = [
    path('profile/', firstAPI),
]
