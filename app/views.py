from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.mockData import mockExercises
from . import forms
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'app/home.html', context)


def exercises(request):
    context = {
        'exercises': mockExercises.exercise_list,
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
