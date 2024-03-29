from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Empleado
# from django.core.validators import MinValueValidator
# from django.utils import timezone

# Create your models here.

class Activo(models.Model):
    idactivo = models.CharField(max_length=6, primary_key=True, verbose_name='Activo')
    serial = models.CharField(max_length=25, verbose_name="Serial")
    so = models.CharField(max_length=10, verbose_name="Sistama operativo")
    marca = models.CharField(max_length=25, verbose_name="Marca")
    tipo = models.CharField(max_length=10, verbose_name="Tipo de dispositivo")
    fecha = models.DateField(auto_now_add=True)
    observaciones = models.TextField(max_length=200, verbose_name="Caracteristicas")
    class EstadoActivo(models.TextChoices):
        nuevo='Nuevo', _('Nuevo')
        usado='Usado', _('Usado')
        reparado='Reparado', _('Reparado')
        otro='Otro', _('Otro')
    situacion =models.CharField(max_length=10, choices=EstadoActivo.choices, default=EstadoActivo.otro, verbose_name="Estado activo")
    class Estado(models.TextChoices):
        asignado='1', _('Asignado')
        creado='0', _('Creado')
    estado = models.CharField(max_length=1,choices=Estado.choices, default=Estado.creado, verbose_name='Estado')
    empleado =models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False, verbose_name="Empleado")

    def __str__(self)->str:
        return "%s" %(self.idactivo)
    


        

    

