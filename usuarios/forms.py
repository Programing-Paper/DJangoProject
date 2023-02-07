from django.forms import ModelForm, widgets
from django import forms 
from usuarios.models import Empleado, Cargo


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        exclude = ['estado']

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'