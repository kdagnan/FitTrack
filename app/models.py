from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Food_Entry(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=300)
    calories = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description