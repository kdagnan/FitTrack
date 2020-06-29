from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class WeightLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    weight = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.timestamp) + ' ' + self.user.username