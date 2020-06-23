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
food_list_old = [
    {
        'date': date.today(),
        'food': [
            {
                'time': '1:00',
                'description': 'ham sandwich',
                'calories': 500
            },
            {
                'time': '14:05',
                'description': 'coke',
                'calories': 360
            }
        ]
    },
    {
        'date': date.today() - timedelta(days=1),
        'food': [
            {
                'time': '14:00',
                'description': 'ice cream',
                'calories': 1000
            },
            {
                'time': '11:50',
                'description': 'peanut butter',
                'calories': 360
            }
        ]
    }
]

food_list = [
    {
        'date': datetime.now().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'ham sandwich',
        'calories': 500
    },
    {
        'date': datetime.now().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'coke',
        'calories': 360
    },
    {
        'date': (datetime.now() - timedelta(days = 1)).date().strftime('%-m/%-d/%y'),
        'time': datetime.now().time().strftime('%H:%M'),
        'description': 'ice cream',
        'calories': 1000
    }
]

def foodtracker(request):
    for d in food_list_old:
        sum = 0
        for f in d['food']:
            sum = sum + f['calories']
        d.update({"total_calories": sum})
    
    storage = {}
    for d in food_list:
        if d['date'] in storage:
            storage[d['date']].append(d)
        else:
            storage[d['date']] = [d]

    context = {
        'title': 'Food Tracker',
        'data': food_list_old,
        'new_data': food_list,
        'storage': storage
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