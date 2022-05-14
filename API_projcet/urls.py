from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authentication import TokenAuthentication

from API_app.views import BlogUpdateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('login-token/', obtain_auth_token),
    path('app/', include('API_app.urls')),
    path('obtain-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    
]
urlpatterns += static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, Document_root=settings.STATIC_ROOT)
