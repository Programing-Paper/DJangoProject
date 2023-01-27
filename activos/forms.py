from django.forms import ModelForm
from activos.models import Activo

class ActivoForm(ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'

