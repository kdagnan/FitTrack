from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import ExerciseLog, Exercise

# Create your views here.
def home(request):
    context = {
        'exercise_logs' : ExerciseLog.objects.filter(user=request.user.id),
        'exercises' : Exercise.objects.all(),
        'title' : 'Exercise Log',
        'user_id' : request.user.id,
    }
    return render(request, 'exlog_app/home.html', context)

# Exlog List View too complicated using class based view
class ExlogDetailView(DetailView):
    model = ExerciseLog
    context_object_name = "exlog"


