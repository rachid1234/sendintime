from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, welcome_page

urlpatterns = [
    path("", welcome_page, name="welcome_page"),
    path("admin/", admin.site.urls),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
