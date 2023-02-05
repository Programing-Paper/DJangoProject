from django.forms import ModelForm, widgets
from django import forms
from usuarios.models import Empleado


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        exclude = ['estado']

