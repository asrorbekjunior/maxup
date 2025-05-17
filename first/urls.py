from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("adm1n/", admin.site.urls),
    path("", include("main.urls")),
    path("select2/", include("django_select2.urls")),  # Select2 uchun URL
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
