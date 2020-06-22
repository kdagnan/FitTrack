from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='exlog_home'),
    path('routetest/', views.template_test, name='exlog_route_test')
]