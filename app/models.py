from django.db import models
<<<<<<< HEAD
#from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    group = models.CharField(max_length=100)
    group_code = models.IntegerField()
    description = models.TextField()
    image_link = models.TextField()




=======
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class WeightLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    weight = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.timestamp) + ' ' + self.user.username
>>>>>>> 06c1cd496f40eb88f32564cb134a2bf87998c98d
