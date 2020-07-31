from django.urls import path
from django.contrib.auth import views as django_views
from . import views, forms


app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('exercises/', views.exercises, name='exercises'),
    path('exercises/<int:active_exercises>', views.exercises, name='exercises'),
    path('foodtracker/', views.foodtracker, name='foodtracker'),
    path('weightlog/', views.weightlog, name='weightlog'),
    path('results/', views.results, name='results'),
    path('login/', django_views.LoginView.as_view(template_name='app/login.html',
                                                  authentication_form=forms.UserAuthenticationForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup')
]
