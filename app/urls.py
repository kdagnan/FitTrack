from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exercises/', views.exercises, name='exercises'),
    path('exerciselog/', views.exerciselog, name='exerciselog'),
    path('foodtracker/', views.foodtracker, name='foodtracker'),
    path('results/', views.results, name='results'),
    path('login/', views.login, name='login')
]
