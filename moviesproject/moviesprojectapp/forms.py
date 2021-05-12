from django import forms
from . models import movie


class movieForm(forms.ModelForm):
    class Meta:
        model = movie #the model name
        fields = ['name', 'desc', 'year', 'image']

