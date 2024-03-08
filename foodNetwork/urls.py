from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('webapp.urls')),
]

# Serve media files during development only
if settings.DEBUG:
    # Include media patterns with optional prefixes (/mobile/ or /desktop/)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/mobile/' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/desktop/' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    