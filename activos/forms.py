from django.forms import ModelForm, widgets
from django import forms
from activos.models import Activo

class ActivoForm(ModelForm):
    class Meta:
        model = Activo
        # fields = '__all__'
        exclude = ['estado', 'idempleado']
        widgets={
          'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        }

class UpdateForm(ModelForm):
    class Meta:
        model = Activo
        exclude = ['estado', 'idactivo', 'idempleado']
        
# class AsignarForm(forms.Form):
#   fecha= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))
# 

class AsignarForm(ModelForm):
    class Meta:
        model = Activo
        exclude = ['idactivo', 'serial', 'so', 'tipo', 'marca', 'observaciones', 'estado', 'situacion']
        # fields = '__all__'
        # widgets={
        #   'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'),
        # }