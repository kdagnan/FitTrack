from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Food_Entry
from .forms import FoodForm
from .models import Exercise
from .models import WeightLog
from .forms import WeightLogForm
from . import forms
from django.contrib.auth import login, authenticate
import json, os

def button_class(active_exercise, button):
    if active_exercise == button:
        return 'btn btn-outline-primary btn-sm active'
    else:
        return 'btn btn-outline-primary btn-sm'


# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'app/home.html', context)


def exercises(request, active_exercises=0):
    classes = {
        'button1_class': button_class(active_exercises, 1),
        'button2_class': button_class(active_exercises, 2),
        'button3_class': button_class(active_exercises, 3),
        'button4_class': button_class(active_exercises, 4),
        'button5_class': button_class(active_exercises, 5),
        'button6_class': button_class(active_exercises, 6),
        'button7_class': button_class(active_exercises, 7),
        'button8_class': button_class(active_exercises, 8),
        'button9_class': button_class(active_exercises, 9),
        'button10_class': button_class(active_exercises, 10),
        'button11_class': button_class(active_exercises, 11),
        'button12_class': button_class(active_exercises, 12),
    }

    body_diagram = "/static/bodyDiagram/bodyDiagram" + str(active_exercises) + ".png"
    

    exercise_list = []

    with open(os.path.dirname(os.path.realpath(__file__)) + '/Exercises.json') as f:
        data = json.load(f)

    if (active_exercises == 100):
        #exercise_list = Exercise.objects.all()
        exercise_list = data
    else:
        #exercise_list = Exercise.objects.filter(group_code=active_exercises)
        for item in data:
            if item["group_code"] == active_exercises:
                exercise_list.append(item)

    context = {
        'exercises': exercise_list,
        'title': 'Exercises',
        'active_exercise': active_exercises, #exercise_list[0].group,
        'classes': classes,
        'body_diagram': body_diagram,
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


def weightlog(request):
    form = WeightLogForm()
    context = {
        'title': 'Weight Log',
        'weight_logs': WeightLog.objects.filter(user=request.user).order_by('-timestamp'),
        'form': form
    }
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            w = WeightLog(weight=form.cleaned_data['weight'], user=request.user)
            w.save()
            return render(request, 'app/weightlog.html', context)
    else: 
        return render(request, 'app/weightlog.html', context)


def results(request):
    context = {
        'title': 'Results'
    }
    return render(request, 'app/results.html', context)


def login_view(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'app/login.html', context)


def signup(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = forms.UserRegistrationForm()

    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'app/signup.html', context)
