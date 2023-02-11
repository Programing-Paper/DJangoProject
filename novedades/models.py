from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Empleado
from activos.models import Activo

# Create your models here.
 

class Novedad(models.Model):
    fecha = models.DateField( auto_now_add=True, verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")
    empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False, verbose_name="Empleado")
    class Estadonovedad(models.TextChoices):
        resuelto='1', _('Resuelo')
        pendiente='0', _('Pendiente')
    estado=models.CharField(max_length=1, choices=Estadonovedad.choices, default=Estadonovedad.pendiente, verbose_name="Estado")
    descripcion=models.TextField(max_length=200, verbose_name="Descripcion")
    activo=models.ForeignKey(Activo , on_delete=models.CASCADE,null=True,blank=False,verbose_name="Activo")
