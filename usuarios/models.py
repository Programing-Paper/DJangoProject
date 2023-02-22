from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.

class Cargo(models.Model):
    nomcargo = models.CharField(max_length=70, verbose_name='Cargo')
    sueldo = models.CharField(max_length=10, blank=True, verbose_name='Sueldo')
    def __str__(self)->str:
        return "%s" %(self.nomcargo)
   
class Empleado(models.Model):
    documento = models.CharField(max_length=11, primary_key=True, verbose_name="Documento de Identidad")
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    correo= models.EmailField(max_length=150, verbose_name="Correo")
    perfil= models.ImageField(upload_to='images/usuarios', blank=True, default='images/usuarios/default.png')
    cargoid=models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=False , null=True, verbose_name="Cargo")
    class Ciudad(models.TextChoices):
        medellin='medellin', _('Medellin')
        bogota='bogota', _('Bogota')
        cucuta='cucuta', _('Cucuta')
        cartagena='cartagena', _('Cartagena')
        bucaramanga='bucaramanga', _('Bucaramanga')
        otro='otro', _('Otro')
    compania=models.CharField(max_length=30, choices=Ciudad.choices, default=Ciudad.otro, verbose_name="Compañia")
    class Estadoempleado(models.TextChoices):
        activo='1', _('Activo')
        inactivo='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estadoempleado.choices, default=Estadoempleado.activo, verbose_name="Estado empleado")
    telefono=models.CharField(max_length=150, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    # fecha_nacimiento=models.DateField(verbose_name="Fecha", help_text=u"MM/DD/AAAA")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self)->str:
        return "%s" %(self.nombres)






        
    



    