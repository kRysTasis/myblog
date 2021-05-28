from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myblog.urls')),
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
