from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, linked_in_login, welcome_page

urlpatterns = [
    #path("", image_upload, name="upload"),
    path("code/", linked_in_login, name="linkedin_profile"),
    path("", welcome_page, name="welcome_page"),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
