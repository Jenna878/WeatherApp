from dataclasses import fields
from tkinter.ttk import Widget
from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name'] 
        widgets = {'name' : TextInput(attrs={
            'class': 'form-control', 
            'name':'city',
            'id': 'city',
            'placeholder': 'введите город'
        })}