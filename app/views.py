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
    context = {
        'title': 'Home'
    }
    return render(request, 'app/home.html', context)


def exercises(request):
    context = {
        'exercises': exercise_list,
        'title': 'Exercises'
    }
    return render(request, 'app/exercises.html', context)


def exerciselog(request):
    context = {
        'title': 'Exercise Log'
    }
    return render(request, 'app/exerciselog.html', context)


def foodtracker(request):
    context = {
        'title': 'Food Tracker'
    }
    return render(request, 'app/foodtracker.html', context)

def weighttracker(request):
    context = {
        'title': 'Weight Tracker'
    }
    return render(request, 'app/weighttracker.html', context)


def results(request):
    context = {
        'title': 'Results'
    }
    return render(request, 'app/results.html', context)


def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'app/login.html', context)
