from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator

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
    alpha_num_dash = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters and dashes are allowed.')
    exercise_name = models.CharField(max_length=32, validators=[alpha_num_dash])
    num_sets = models.PositiveIntegerField()
    num_reps = models.PositiveIntegerField()
    exercise_weight = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.exercise_log) + "\t" + str(self.exercise_name) + "\t" + str(self.num_sets) + "x" + str(self.num_reps) + "\t" + str(self.exercise_weight)

    def get_absolute_url(self):
        return reverse('exlog-detail', kwargs={'pk': self.exercise_log.id})
    

