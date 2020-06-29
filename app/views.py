from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Exercise

def button_class(active_exercise, button):
    if (active_exercise ==  button):
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
    exercise_list = Exercise.objects.filter(group_code=active_exercises)

    context = {
        'exercises': exercise_list,
        'title': 'Exercises',
        'active_exercise': exercise_list[0].group,
        'classes': classes,
        'body_diagram': body_diagram,
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
