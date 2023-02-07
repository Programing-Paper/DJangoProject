from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Empleado

# from django.core.validators import MinValueValidator
# from django.utils import timezone

# Create your models here.

class Activo(models.Model):
    idactivo = models.CharField(max_length=6, primary_key=True, verbose_name='Numero activo')
    serial = models.CharField(max_length=25, verbose_name="Serial")
    so = models.CharField(max_length=10, verbose_name="Sistama operativo")
    marca = models.CharField(max_length=25, verbose_name="Tipo de dispositivo")
    tipo = models.CharField(max_length=10, verbose_name="Caracteristicas")
    fecha = models.DateField(auto_now_add=True)
    observaciones = models.TextField(max_length=200, verbose_name="Caracteristicas")
    class EstadoActivo(models.TextChoices):
        nuevo='3', _('Nuevo')
        usado='2', _('Usado')
        reparado='1', _('Reparado')
        disponible='0', _('Disponible')
    situacion =models.CharField(max_length=1, choices=EstadoActivo.choices, default=EstadoActivo.disponible, verbose_name="Estado activo")
    class Estado(models.TextChoices):
        asignado='1', _('Asignado')
        creado='0', _('Creado')
    estado = models.CharField(max_length=1,choices=Estado.choices, default=Estado.creado, verbose_name='Estado')
    empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False, verbose_name="Empleado")




    

