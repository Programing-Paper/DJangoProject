from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Empleado

# Create your models here.
 

class Novedad(models.Model):
    fecha = models.DateField(verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")
    empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False, verbose_name="Empleado")
    class Estadonovedad(models.TextChoices):
        RESUELTO='1', _('Resuelo')
        PENDIENTE='0', _('Pendiente')
    estado=models.CharField(max_length=1, choices=Estadonovedad.choices, default=Estadonovedad.PENDIENTE, verbose_name="Estado")
    descripcion=models.TextField(max_length=200, verbose_name="Descripcion")
    # activoid=models.ForeignKey(Activo , on_delete=models.CASCADE,null=True,blank=False,verbose_name="Activo")

