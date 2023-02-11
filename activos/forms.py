from django.forms import ModelForm, widgets
from django import forms
from activos.models import Activo
from usuarios.models import Empleado

class ActivoForm(ModelForm):
    class Meta:
        model = Activo
        # fields = '__all__'
        exclude = ['estado']
        widgets={
          'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        }

# class AsignarForm(forms.Form):
#   fecha= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))


class AsignarForm(ModelForm):
    class Meta:
        model = Activo
        exclude = ['idactivo', 'serial', 'so', 'tipo', 'marca', 'observaciones', 'estado', 'situacion']
        fields = '__all__'
        widgets={
          'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        }