from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.static import serve
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myblog.urls')),
    # path('markdownx/', include('markdownx.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += [path('<path:path>', TemplateView.as_view(template_name='index.html'))]
