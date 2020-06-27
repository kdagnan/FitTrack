from django.urls import path
from .views import ExlogListView
from . import views

urlpatterns = [
    path('', views.home, name='exlog_home'),
    path('listview/', ExlogListView.as_view(), name='exlog_listview'),
    path('routetest/', views.template_test, name='exlog_route_test')
]