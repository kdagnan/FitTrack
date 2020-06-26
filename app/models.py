from django.db import models
from django.utils import timezone

# Create your models here.

class Food_Entry(models.Model):
    datetime = date = models.DateTimeField(default=timezone.now)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    calories = models.IntegerField()

    def __str__(self):
        return self.description