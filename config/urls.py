from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.defaults import page_not_found

# Custom 404 handler (works when DEBUG=False in production)
handler404 = 'config.urls.custom_404'

def custom_404(request, exception=None):
    return page_not_found(request, exception, template_name='404.html')

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=True
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Preview 404 page during development
    urlpatterns += [path('404/', custom_404)]
