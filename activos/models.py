from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Empleado
# ñ
# from django.core.validators import MinValueValidator
# from django.utils import timezone

# Create your models here.

class Activo(models.Model):
    empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False,verbose_name="Empleadoid")
    class EstadoActivo(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado =models.CharField(max_length=1, choices=EstadoActivo.choices, default=EstadoActivo.ACTIVO, verbose_name="Estadoactivo")
    serial = models.CharField(max_length=25)
    so = models.CharField(max_length=10)
    marca = models.CharField(max_length=25)
    tipo = models.CharField(max_length=10)
    fecha = models.DateField(verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")
    observaciones = models.CharField(max_length=200)
    class Estado(models.TextChoices):
        asignado='1', _('Asignado')
        pendiente='0', _('Pendiente')
    estado = models.CharField(max_length=1,choices=Estado.choices, default=Estado.pendiente, verbose_name='Estado')



    

