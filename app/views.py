from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("home")


def exercises(request):
    return HttpResponse("exercises")


def exerciselog(request):
    return HttpResponse("exercise log")


def foodtracker(request):
    return HttpResponse("food tracker")


def results(request):
    return HttpResponse("results")


def login(request):
    return HttpResponse("log in")
