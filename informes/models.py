from django.db import models
from usuarios.models import Empleado
from activos.models import Activo

# Create your models here.

class Movimientos(models.Model):
    empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False,verbose_name="Empleado")
    activoid=models.ForeignKey(Activo , on_delete=models.CASCADE,null=True,blank=False,verbose_name="Activo")
    fechaint = models.DateField(help_text=u"MM/DD/AAAA", verbose_name="Fecha registro")  
    fechaout = models.DateField(help_text=u"MM/DD/AAAA", verbose_name="Fecha salida")
    descripcion= models.CharField(max_length=200, verbose_name='Descripcion')



