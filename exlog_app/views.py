from django.shortcuts import render
from django.contrib.auth.models import User
from exlog_app.models import ExerciseLog, Exercise

exlog_test_data = [
    {
        'exercise' : 'deadlift',
        'sets' : '4',
        'reps' : '8',
        'weight' : '135'
    },
    {
        'exercise' : 'squat',
        'sets' : '4',
        'reps' : '8',
        'weight' : '130'
    },
        {
        'exercise' : 'leg press',
        'sets' : '4',
        'reps' : '10',
        'weight' : '160'
    }
]

# Create your views here.
def home(request):
    context = {
        'exercise_logs' : ExerciseLog.objects.all(),
        'exercises' : Exercise.objects.all(),
        'title' : 'Exercise Log',
        'user_name' : 'John'
    }
    return render(request, 'exlog_app/home.html', context)

def template_test(request):
    return render(request, 'exlog_app/home.html', {'title' : 'TESTING'})

