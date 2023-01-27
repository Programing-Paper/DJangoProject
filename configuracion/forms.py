from django.forms import ModelForm
from configuracion.models import Admin

class AdminForm(ModelForm):
    class Meta:
        model= Admin
        # fields='__all__'
        exclude=['Userestado']

