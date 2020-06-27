from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import ExerciseLog, Exercise

# Create your views here.
def home(request):
    context = {

        # By default, the home page loads all the workout logs in existence
        'exercise_logs' : ExerciseLog.objects.all(),
        'exercises' : Exercise.objects.all(),
        'title' : 'Exercise Log',
        'user_name' : User.objects.first().username,
        'today_workout' : True,
    }
    return render(request, 'exlog_app/home.html', context)

class ExlogListView(ListView):
    model = ExerciseLog
    template_name = "exlog/"

def template_test(request):
    return render(request, 'exlog_app/home.html', {'title' : 'TESTING'})

