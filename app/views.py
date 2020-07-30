from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Food_Entry
from exlog_app.models import ExerciseLog, Exercise as Exercise_App
from .forms import FoodForm
from django.db.models import Avg, Count
from .forms import FoodFormTheSecond
from .models import Exercise
from .models import WeightLog
from .forms import WeightLogForm
from . import forms
from django.contrib.auth import login, authenticate
import io
import urllib, base64
import matplotlib.pyplot as plt
import json, os, matplotlib
import numpy as np

import matplotlib

def button_class(active_exercise, button):
    if active_exercise == button:
        return 'btn btn-outline-secondary btn-sm active'
    else:
        return 'btn btn-outline-secondary btn-sm'


# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'app/home.html', context)


def exercises(request, active_exercises=0):
    classes = {
        'button1_class': button_class(active_exercises, 102),
        'button2_class': button_class(active_exercises, 106),
        'button3_class': button_class(active_exercises, 103),
        'button4_class': button_class(active_exercises, 110),
        'button5_class': button_class(active_exercises, 111),
        'button6_class': button_class(active_exercises, 112),
        'button7_class': button_class(active_exercises, 113),
        'button8_class': button_class(active_exercises, 114),
        'button9_class': button_class(active_exercises, 117),
        'button10_class': button_class(active_exercises, 118),
        'button11_class': button_class(active_exercises, 120),
        'button12_class': button_class(active_exercises, 121),
        'button13_class': button_class(active_exercises, 119),
        'button14_class': button_class(active_exercises, 101),
        'button15_class': button_class(active_exercises, 104),
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
    # Handling form submissions
    if request.method == 'POST' and 'sub_btn_1' in request.POST:
        form_sub = FoodForm(request.POST)
        if form_sub.is_valid():
            # Ensuring calories match description if already in database
            val = True
            if Food_Entry.objects.filter(user=request.user, description=form_sub.cleaned_data['description']).exists():
                old_entry = Food_Entry.objects.filter(user=request.user, description=form_sub.cleaned_data['description']).first()
                if old_entry.calories != form_sub.cleaned_data['calories']:
                    messages.error(request, "ERROR: Reused descriptions must match calories!", extra_tags='danger')
                    val = False
                else:
                    f = Food_Entry(date=form_sub.cleaned_data['date'], description=form_sub.cleaned_data['description'], calories=form_sub.cleaned_data['calories'], user=request.user)
                    f.save()
            # Ensuring calories are 0 or greater
            if form_sub.cleaned_data['calories'] < 0:
                messages.error(request, "ERROR: Calories must be greater or equal to 0!", extra_tags='danger')
                val = False
            if val == True:
                f = Food_Entry(date=form_sub.cleaned_data['date'], description=form_sub.cleaned_data['description'], calories=form_sub.cleaned_data['calories'], user=request.user)
                f.save()
                messages.success(request, "Successfully added " + form_sub.cleaned_data['description'] + ".", extra_tags='success')
        else:
            messages.error(request, "ERROR: Description may only contain alphanumerics, end stops, commas, and parentheses!", extra_tags='danger')
    elif request.method == 'POST' and 'sub_btn_2' in request.POST:
        form_sub = FoodFormTheSecond(request.POST, request=request)
        if form_sub.is_valid():
            f = Food_Entry.objects.filter(user=request.user, description=form_sub.cleaned_data['description']).first()
            f.pk = None
            f.date = form_sub.cleaned_data["date"]
            f.save()
            messages.success(request, "Successfully added " + form_sub.cleaned_data['description'] + ".", extra_tags='success')
    elif request.method == 'POST':
        f = Food_Entry.objects.filter(user=request.user, pk=request.POST['pk']).first()
        Food_Entry.objects.filter(user=request.user, pk=request.POST['pk']).delete()
        messages.success(request, "Successfully deleted " + f.description + ".", extra_tags='success')
    # Creating forms
    form = FoodForm()
    form_2 = FoodFormTheSecond(request=request)

    # Getting data
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

    # Passing info
    context = {
        'title': 'Food Tracker',
        'data': data,
        'form': form,
        'form_2': form_2,
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
        'form': form,
        'savedWeight': False
    }
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            w = WeightLog(weight=form.cleaned_data['weight'], user=request.user)
            w.save()
            context['savedWeight'] = True
            return render(request, 'app/weightlog.html', context)
    else: 
        return render(request, 'app/weightlog.html', context)


def results(request):

    # Weight Plot
    matplotlib.use('Agg')
    plt.close()
    plt.plot([i.timestamp.date().__format__('%-m/%-d') for i in WeightLog.objects.filter(user=request.user).order_by('timestamp')], [int(i.weight) for i in WeightLog.objects.filter(user=request.user).order_by('timestamp')], marker='o', markersize=5, color='blue')
    plt.xlabel('Date')
    plt.ylabel('Weight (lbs)')
    fig1 = plt.gcf()
    buf1 = io.BytesIO()
    fig1.savefig(buf1, format='png')
    buf1.seek(0)
    string = base64.b64encode(buf1.read())
    img1 = urllib.parse.quote(string)
    plt.close()

    list = Food_Entry.objects.filter(user=request.user).order_by('date').extra({'_date': 'Date(date)'}).values(
         '_date').annotate(val=Avg('calories'), count=Count('calories'))

    dates = []
    cals = []
    counts = []
    avgCals = 0
    for item in list:
        print(item)
        date = item.get('_date')
        date = date.split('-')
        dates.append(date[1] + '-' + date[2])
        cals.append(item.get('val'))
        counts.append(item.get('count'))
        avgCals = avgCals + item.get('val') * item.get('count')
    if len(dates) > 0:
        avgCals = avgCals / len(dates)

    # Calorie Plot
    plt.plot([i for i in dates],
             [int(j * counts[i]) for i,j in enumerate(cals)],
             marker='o', markersize=5, color='blue')
    plt.xlabel('Date')
    plt.ylabel('Calories Consumed')
    fig2 = plt.gcf()
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    string = base64.b64encode(buf2.read())
    img2 = urllib.parse.quote(string)
    plt.close()

    ex_names = []
    for i in ExerciseLog.objects.filter(user=request.user):
        for j in Exercise_App.objects.filter(exercise_log=i):
            ex_names.append(j.exercise_name)

    weights = []
    reps = []
    dates = []
    rep_max = []
    for i in ExerciseLog.objects.filter(user=request.user).order_by('date'):
        for j in Exercise_App.objects.filter(exercise_log=i):
            if j.exercise_name == request.GET.get('ex', ''):
                weights.append(j.exercise_weight)
                reps.append(j.num_reps)
                dates.append(i.date)

                # Epley formula for 1RM calculation
                rep_max.append(int(j.exercise_weight * (1 + j.num_reps / 30)))

    # Strength Plot
    plt.plot([i.__format__('%-m/%-d') for i in dates], [i for i in rep_max], marker='o', markersize=5, color='blue')
    plt.title(request.GET.get('ex', 'Select an exercise'))
    plt.xlabel('Date')
    plt.ylabel(request.GET.get('ex', '') + ' (1 Repetition Maximum)')

    if len(rep_max) > 0:
        plt.ylim(min(rep_max) - 10, max(rep_max) + 10)

    for i in range(0, len(dates)):
        plt.annotate(int(rep_max[i]), (dates[i].__format__('%-m/%-d'), rep_max[i]+2), ha="center")

    fig3 = plt.gcf()
    buf3 = io.BytesIO()
    fig3.savefig(buf3, format='png')
    buf3.seek(0)
    string = base64.b64encode(buf3.read())
    img3 = urllib.parse.quote(string)
    plt.close()

    weightSum = 0
    for i in WeightLog.objects.filter(user=request.user):
        weightSum += int(i.weight)

    if len(WeightLog.objects.filter(user=request.user)) > 0:
        average = weightSum / (len(WeightLog.objects.filter(user=request.user)))
        average = '%.2f' % average
        change = int(WeightLog.objects.filter(user=request.user)[len(WeightLog.objects.filter(user=request.user)) - 1].weight) - int(WeightLog.objects.filter(user=request.user)[0].weight)
    else:
        average = '--'
        change = '--'

    if len(rep_max) > 0:
        str_change = ((rep_max[len(rep_max) - 1] - rep_max[0]) / rep_max[0]) * 100
        str_change = '%.2f' % str_change
    else:
        str_change = '--'

    print(cals)
    context = {
        'title': 'Results',
        'img1': img1,
        'img2': img2,
        'img3': img3,
        'change': change,
        'average': average,
        'ex_names': np.unique(np.array(ex_names)),
        'str_change': str_change,
        'avg_cals': avgCals
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