from django import forms
from .views import Exercise

class ExerciseCreateForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('exercise_name', 'num_sets', 'num_reps', 'exercise_weight')
