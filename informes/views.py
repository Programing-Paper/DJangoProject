from django.shortcuts import render
from activos.models import Activo
from novedades.models import Novedad
# from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.


def informes(request):
    title= 'informes'

    activos_nuevos= Activo.objects.filter(situacion='Nuevo').count()
    activos_usados= Activo.objects.filter(situacion='Usado').count()
    activos_reparados= Activo.objects.filter(situacion='Reparado').count()
    activos_otros= Activo.objects.filter(situacion='Otro').count()

    labels_stock= [activos_nuevos, activos_usados, activos_reparados, activos_otros] 

    novedades_pendientes = Novedad.objects.filter(estado='Pendiente').count()
    novedades_resueltos = Novedad.objects.filter(estado='Resuelto').count()

    novedades_estado = [novedades_pendientes, novedades_resueltos]

    gerentes = Group.objects.filter(name='Gerente').count()
    normales = Group.objects.filter(name='Normal').count()

    roles = [normales, gerentes]

    context={
        'title': title,
        'labels_stock': labels_stock,
        'roles': roles,
        'estado': novedades_estado      
    }
    return render(request,'informes/informes.html', context)