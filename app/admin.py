from django.contrib import admin
from .models import Food_Entry
from .models import Exercise
from .models import WeightLog
# Register your models here.

admin.site.register(Exercise)
admin.site.register(WeightLog)
admin.site.register(Food_Entry)
