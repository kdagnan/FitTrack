from django.shortcuts import render
from django.views.generic import DetailView, CreateView
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

    # Getting extra context for the class-based view
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)        
        
        # The line below literally took me hours to figure out
        context['exercises'] = Exercise.objects.filter(exercise_log=self.object).iterator()
        return context

class ExlogCreateView(CreateView):
    model = ExerciseLog
    fields = ['date']

    def form_valid(self, form):
        form.instance.user = self.request.user_id
        return super().form_valid(form)