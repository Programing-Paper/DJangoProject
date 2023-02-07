from django.db import models
from django.utils.translation import gettext_lazy as _
# from usuarios.models import Empleado

# Create your models here.

class Admin(models.Model):
    correo= models.CharField(max_length=50, verbose_name="Correo")
    password= models.CharField(max_length=50, verbose_name="Contraseña")
    perfil= models.CharField(max_length=255, verbose_name="Profile")
    class Estadouser(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    userestado= models.CharField(max_length=1, verbose_name="Estado")
    # empleadoid=models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Empleado")


