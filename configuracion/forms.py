from django.forms import ModelForm
from django import forms
from configuracion.models import Admin

class AdminForm(ModelForm):
    class Meta:
        model= Admin
        exclude=['empleadoid']

class UpdateProfile(forms.Form):
    correo = forms.CharField(label="Correo Actual", max_length=60,)



