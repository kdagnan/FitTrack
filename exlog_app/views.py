from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.http import HttpResponseRedirect
from .models import ExerciseLog, Exercise

# List all Exercise Logs owned by the user
def home(request):
    context = {
        'exercise_logs' : ExerciseLog.objects.filter(user=request.user.id),
        'exercises' : Exercise.objects.all(),
        'title' : 'Exercise Log',
        'user_id' : request.user.id,
    }

    # If the user does not have any Workout Logs
    if not context['exercise_logs'].count():
        return render(request,'exlog_app/get_started.html')

    # Otherwise, load the list view of all Exercise Logs owned by the user
    return render(request, 'exlog_app/home.html', context)

def add_from_recommender(request, exercise_name):
    print(exercise_name)

    today_log = None
    # Incase there has not been a workout log created for the current day
    try:
        today_log = ExerciseLog.objects.filter(user=request.user.id, date=datetime.date.today())[0]
    
    # There is no exercise log created for the current day
    except IndexError:

        # Create a new exercise log for today for the current user
        today_log = ExerciseLog.objects.create(
            user=request.user,
            date=datetime.date.today(),
        )

    except Exception as e:
        print('ERROR', e)

    # Create the exercise
    Exercise.objects.create(
        exercise_log=today_log,
        exercise_name= exercise_name,
        num_sets=0,
        num_reps=0,
        exercise_weight=0,
    )

    # Redirects to today's workout log after adding the exercise
    return HttpResponseRedirect("/exlog/log/"+str(today_log.id))

# Detail View for Exercise Log objects
class ExlogDetailView(DetailView):
    model = ExerciseLog
    context_object_name = "exlog"

    # Getting extra context for the class-based view
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)        
        
        # The line below literally took me hours to figure out
        context['exercises'] = Exercise.objects.filter(exercise_log=self.object).iterator()
        return context

# Class based view for Create (Exercise Log)
class ExlogCreateView(LoginRequiredMixin, CreateView):
    model = ExerciseLog
    fields = ['date']

    def get_form(self):
        form = super(ExlogCreateView, self).get_form()
        initial_base = self.get_initial() 
        initial_base['date'] = timezone.now().strftime('%-m/%-d/%Y')
        form.initial = initial_base
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Class based view for Update
class ExlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExerciseLog
    fields = ['date']

    def get_form(self):
        form = super(ExlogUpdateView, self).get_form()
        initial_base = self.get_initial() 
        initial_base['date'] = timezone.now().strftime('%-m/%-d/%Y')
        form.initial = initial_base
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Test to see if current logged in user is the creator of the workout log
    def test_func(self):
        exlog = self.get_object()
        if self.request.user == exlog.user:
            return True
        return False

# Class based view for Delete (Exercise Log)
class ExlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ExerciseLog
    context_object_name = "exlog"
    success_url = '/exlog/'   
    
    # Test to see if current logged in user is the creator of the workout log
    def test_func(self):
        exlog = self.get_object()
        if self.request.user == exlog.user:
            return True
        return False

# Class based view for Create (Exercise)
class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['exercise_name', 'num_sets', 'num_reps', 'exercise_weight']

    def form_valid(self, form):
        form.instance.exercise_log = ExerciseLog.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

# Class based view for Update (Exercise)
class ExerciseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exercise
    fields = ['num_sets', 'num_reps', 'exercise_weight']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Test to see if current logged in user is the creator of the workout log
    def test_func(self):
        exlog = self.get_object()
        if self.request.user == exlog.exercise_log.user:
            return True
        return False

# Class based view for Delete
class ExerciseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Exercise
    success_url = '/exlog/'   
    
    # Test to see if current logged in user is the creator of the workout log
    def test_func(self):
        exlog = self.get_object()
        if self.request.user == exlog.exercise_log.user:
            return True
        return False