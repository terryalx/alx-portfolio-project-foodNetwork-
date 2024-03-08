from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.ListModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/<int:pk>/', views.ListModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
