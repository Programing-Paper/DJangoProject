from django.db import models
from usuarios.models import Empleado
from activos.models import Activo

# Create your models here.

class Movimientos(models.Model):
    empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE,null=True,blank=False,verbose_name="Empleadoid")
    activoid=models.ForeignKey(Activo , on_delete=models.CASCADE,null=True,blank=False,verbose_name="Activoid")
    fechaint = models.DateField(verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")  
    fechaout = models.DateField(verbose_name="Fecha registro", help_text=u"MM/DD/AAAA")
    descripcion= models.CharField(max_length=200, verbose_name='Descripcion')


    

