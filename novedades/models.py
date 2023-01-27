from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
 

class Novedad(models.Model):
    descripcion=models.CharField(max_length=200, verbose_name="Descripcion")
    fecha = models.DateField(verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")
    activoid=models.CharField(max_length=5, verbose_name="Activoid")
    empleadoid=models.CharField(max_length=11, verbose_name='Empleadoid')
    class Estadonovedad(models.TextChoices):
        RESUELTO='1', _('Resuelo')
        PENDIENTE='0', _('Pendiente')
    estado=models.CharField(max_length=1, choices=Estadonovedad.choices, default=Estadonovedad.PENDIENTE, verbose_name="Estadonovedad")
