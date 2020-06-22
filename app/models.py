from django.db import models
#from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    group = models.CharField(max_length=100)
    group_code = models.IntegerField()
    description = models.TextField()
    image_link = models.TextField()




