from django.forms import ModelForm, widgets
from django import forms
from novedades.models import Novedad

class NovedadForm(ModelForm):
    class Meta:
        model = Novedad
        fields = '__all__'
        widgets={
          'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }
