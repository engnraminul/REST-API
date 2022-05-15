from django.urls import path
from .views import BlogCreateAPIView, BlogListAPIView, BlogListCreateAPIView, BlogRetrieveAPIView, ContactAPIView, firstAPI, registrationAPI, BlogUpdateAPIView, BlogRetrieveUpdateAPIView, BlogDestroyAPIView

urlpatterns = [
    path('profile/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
    path('blog/', BlogCreateAPIView.as_view()),
    path('bloglist/', BlogListAPIView.as_view()),
    path('blogcreatelist/', BlogListCreateAPIView.as_view()),
    path('blogdetails/<int:id>/', BlogRetrieveAPIView.as_view()),
    path('updateblog/<int:id>/', BlogUpdateAPIView.as_view()),
    path('detailupdate/<int:id>/', BlogRetrieveUpdateAPIView.as_view()),
    path('blogdelete/<int:id>/', BlogDestroyAPIView.as_view()),

]
