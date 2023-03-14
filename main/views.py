from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib.auth import logout
from activos.models import Activo

# from usuarios.models import Empleado
# from novedades.models import Novedad
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib import messages
# from configuracion.models import Admin
# from django.http import JsonResponse
# from django.contrib.auth import authenticate

def inicio(request):
    titulo="Inicio"
    context = {
        'titulo': titulo,
    }
    return render(request,'index.html',context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

# def loggedIn(request):
#     if request.user.is_authenticate:
#         respuesta:"Ingresado como"+ request.user.username
#     else:
#         respuesta:"No esta autenticado. "
#     return HttpResponse(respuesta)

def signout(request):
    logout(request)
    return redirect("inicio")

def informacion(request):
    context = {}
    return render(request,'informacion.pdf',context)

def recuperar(request):
    context = {}
    return render(request,'recuperar.html',context)











