from django import forms
from django.forms import inlineformset_factory
from .views import Exercise

class ExerciseCreateForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('exercise_name', 'num_sets', 'num_reps', 'exercise_weight')


ExerciseFormSet = inlineformset_factory(ExerciseLog, Exercise, fields=('exercise_name', 'num_sets', 'num_reps', 'exercise_weight'))
formset = ExerciseFormSet(exercise_log=self.object)