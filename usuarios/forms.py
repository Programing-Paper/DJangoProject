from django.forms import ModelForm, widgets
from django import forms 
from usuarios.models import Empleado, Cargo


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        exclude = ['estado', 'user']
        # widgets={
        #     'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        # }

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Empleado
        exclude = ['estado', 'documento','user']
        