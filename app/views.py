from django.shortcuts import redirect, render
from django.http import HttpResponse

exercise_list = [
    {
        'name': 'Push-ups',
        'description': 'An exercise in which a person lies facing the floor and, keeping their back straight, raises their body by pressing down on their hands.'
    },
    {
        'name': 'Pull-ups',
        'description': 'An exercise involving raising oneself with both arms by pulling up against a horizontal bar fixed above the head.'
    }
]

# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def exercises(request):
    context = {
        'exercises': exercise_list
    }
    return render(request, 'app/exercises.html', context)


def exerciselog(request):
    return render(request, 'app/exerciselog.html')


def foodtracker(request):
    return render(request, 'app/foodtracker.html')


def results(request):
    return render(request, 'app/results.html')


def login(request):
    return render(request, 'app/login.html')
