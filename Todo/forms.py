

from django import forms
from django.forms import ModelForm
from .models import *

class DateTimeInput(forms.DateTimeInput):
    input_type = 'time'

class TodoForm(forms.ModelForm):
    class Meta:
      model = TodoModel
      fields = ['name','time']
      widgets = {'time' : DateTimeInput }
    