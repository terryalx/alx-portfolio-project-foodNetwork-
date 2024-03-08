from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import SearchListView, PostDetailView

urlpatterns = [
    path('', views.home, name="index"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe_mobile/', views.subscribe_mobile, name='subscribe_mobile'),
    path('join/', views.join, name='join'),
    path('join_mobile/', views.join_mobile, name='join_mobile'),
    path('success/', views.success, name='success'),
    path('alldeal/', views.alldeal, name='alldeal'),
    path('search/', SearchListView.as_view(), name='search_view'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail_view'),
    path('mobile/', views.mobile_view, name='mobile_view'),
    path('desktop/', views.desktop_view, name='desktop_view'),
    path('live/', views.live, name="live"),
]

# Serve media files during development only
if settings.DEBUG:
    # Include media patterns with optional prefixes (/mobile/ or /desktop/)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/mobile/' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/desktop/' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
