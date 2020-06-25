from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Exercise
#from app.mockData import mockExercises

# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'app/home.html', context)


def exercises(request, active_exercises=1234):
    master_list = []

    for x in str(active_exercises):
        group = Exercise.objects.filter(group_code=int(x))
        master_list.extend(group)

    context = {
        'exercises': master_list,
        'title': 'Exercises',
        'exercises_id': active_exercises,
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
