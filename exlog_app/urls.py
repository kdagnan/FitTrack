from django.urls import path
from .views import ExlogDetailView, ExlogCreateView, ExlogUpdateView, ExlogDeleteView
from .views import ExerciseCreateView, ExerciseUpdateView, ExerciseDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='exlog_home'),
    path('log/<int:pk>/', ExlogDetailView.as_view(), name='exlog-detail'),
    path('log/new/', ExlogCreateView.as_view(), name='exlog-create'),
    path('log/<int:pk>/update/', ExlogUpdateView.as_view(), name='exlog-update'),
    path('log/<int:pk>/delete/', ExlogDeleteView.as_view(), name='exlog-delete'),
    path('log/<int:pk>/addexercise/', ExerciseCreateView.as_view(), name='exlog-add-exercise'),
    path('log/<int:pk>/updateexercise/', ExerciseUpdateView.as_view(), name='exlog-update-exercise'),
    path('log/<int:pk>/deleteexercise/', ExerciseDeleteView.as_view(), name='exlog-delete-exercise'),

    # Path allows an exercise to be added to the workout log
    path('log/add_ex_to_today_log/<str:exercise_name>/', views.add_from_recommender, name='exlog-add-from-recommender')
]