from django.forms import ModelForm, widgets
from django import forms
from activos.models import Activo

class ActivoForm(ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'
        # exclude = ['estado']
        # widgets={
        #   'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        # }


