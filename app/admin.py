from django.contrib import admin
from .models import Exercise
from .models import WeightLog
# Register your models here.

admin.site.register(Exercise)
admin.site.register(WeightLog)