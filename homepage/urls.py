from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "homepage"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('upload', image_view, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

