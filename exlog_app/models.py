from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# ExerciseLog contains many exercises (acts like a list of exercises)
class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.user) + "\t" + str(self.date)
    
    def get_absolute_url(self):
        return reverse('exlog-detail', kwargs={'pk': self.pk})

class Exercise(models.Model):
    exercise_log = models.ForeignKey(ExerciseLog, on_delete=models.CASCADE)

    # In the future, exercise should ideally be a foreign key which can be tied together to track progress
    exercise_name = models.CharField(max_length=32)
    num_sets = models.IntegerField()
    num_reps = models.IntegerField()
    exercise_weight = models.IntegerField()
    
    def __str__(self):
        return str(self.exercise_log) + "\t" + str(self.exercise_name) + "\t" + str(self.num_sets) + "x" + str(self.num_reps) + "\t" + str(self.exercise_weight)

    def get_absolute_url(self):
        return reverse('exlog-detail', kwargs={'pk': self.exercise_log.id})
    

