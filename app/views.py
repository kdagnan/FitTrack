from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Food_Entry
from .forms import FoodForm

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

@login_required
def foodtracker(request):
    if request.method == 'POST':
        form_sub = FoodForm(request.POST)
        if form_sub.is_valid():
            f = Food_Entry(date=form_sub.cleaned_data['date'], description=form_sub.cleaned_data['description'], calories=form_sub.cleaned_data['calories'], user=request.user)
            f.save()
    form = FoodForm()
    entries = Food_Entry.objects.filter(user=request.user).order_by('-date')
    data = {}
    for e in entries:
        if e.date in data:
            data[e.date].append(e)
        else:
            data[e.date] = [e]
    total_calories = {}
    for date in data:
        sum = 0
        for foods in data[date]:
            sum = sum + foods.calories
        total_calories[date] = sum
    context = {
        'title': 'Food Tracker',
        'data': data,
        'form': form,
        'total_calories': total_calories,
        'today_date': timezone.now().date(),
        'yesterday_date': timezone.now().date() - timedelta(days=1)
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