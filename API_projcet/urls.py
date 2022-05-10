from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('app/', include('API_app.urls')),
]
urlpatterns += static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, Document_root=settings.STATIC_ROOT)
