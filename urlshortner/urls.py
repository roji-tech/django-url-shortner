from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

admin.site.site_header = "Url Shortner Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortner.urls')),    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
