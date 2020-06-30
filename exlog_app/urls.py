from django.urls import path
from .views import ExlogDetailView, ExlogCreateView, ExlogUpdateView, ExlogDeleteView, ExerciseCreateView
from . import views

urlpatterns = [
    path('', views.home, name='exlog_home'),
    path('log/<int:pk>/', ExlogDetailView.as_view(), name='exlog-detail'),
    path('log/new/', ExlogCreateView.as_view(), name='exlog-create'),
    path('log/<int:pk>/update/', ExlogUpdateView.as_view(), name='exlog-update'),
    path('log/<int:pk>/delete/', ExlogDeleteView.as_view(), name='exlog-delete'),
    path('log/<int:pk>/addexercise/', ExerciseCreateView.as_view(), name='exlog-add-exercise'),
]