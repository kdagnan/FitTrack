from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

class Exercise(models.Model):
    exercise_log = models.ForeignKey(ExerciseLog, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=32)
    num_sets = models.IntegerField()
    num_reps = models.IntegerField()
    exercise_weight = models.IntegerField()
    

