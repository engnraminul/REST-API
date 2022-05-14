from django.urls import path
from .views import BlogCreateAPIView, BlogListAPIView, BlogListCreateAPIView, ContactAPIView, firstAPI, registrationAPI

urlpatterns = [
    path('profile/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
    path('blog/', BlogCreateAPIView.as_view()),
    path('bloglist/', BlogListAPIView.as_view()),
    path('blogcreatelist/', BlogListCreateAPIView.as_view())
]
