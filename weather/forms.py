from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

class WeatherForm(forms.Form):
    temperature = forms.FloatField(label='Temperatura')
    date = forms.DateTimeField(label='Data')
    city = forms.CharField(label='Cidade', required=False)
    atmosphericPressure = forms.CharField(label='Pressão Atmosférica', required=False)
    humidity = forms.CharField(label='Umidade', required=False)
    weather = forms.CharField(label='Clima', required=False)

