from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date, datetime, timedelta

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

# Placeholder data
food_list = [
    {
        'datetime': datetime.now(),
        'date': datetime.now().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'ham sandwich',
        'calories': 500
    },
    {
        'datetime': datetime.now(),
        'date': datetime.now().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'coke',
        'calories': 360
    },
    {
        'datetime': datetime.now(),
        'date': (datetime.now() - timedelta(days = 1)).date().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'ice cream',
        'calories': 1000
    },
    {
        'datetime': datetime.now(),
        'date': (datetime.now() - timedelta(days = 5)).date().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'oatmeal',
        'calories': 200
    }
]

def foodtracker(request):
    data = {}
    for d in food_list:
        if d['date'] in data:
            data[d['date']].append(d)
        else:
            data[d['date']] = [d]
    
    # TODO: Get totals
    context = {
        'title': 'Food Tracker',
        'data': data,
        'test_cond': True
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