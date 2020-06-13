from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def exercises(request):
    return render(request, 'app/exercises.html')


def exerciselog(request):
    return render(request, 'app/exerciselog.html')


def foodtracker(request):
    return render(request, 'app/foodtracker.html')


def results(request):
    return render(request, 'app/results.html')


def login(request):
    return render(request, 'app/login.html')
