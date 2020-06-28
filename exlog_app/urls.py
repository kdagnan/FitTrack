from django.urls import path
from .views import ExlogDetailView, ExlogCreateView
from . import views

urlpatterns = [
    path('', views.home, name='exlog_home'),
    path('log/<int:pk>', ExlogDetailView.as_view(), name='exlog-detail'),
    path('log/new/', ExlogCreateView.as_view(), name='exlog-create'),
]