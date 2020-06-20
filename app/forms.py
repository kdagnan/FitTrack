from django import forms

class WeightLogForm(forms.Form):
    weight = forms.CharField(label='Enter Weight', max_length=5)