from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
# from django.http import HttpResponse
# from django.http import JsonResponse
# from activos.models import Activo
# from django.contrib.auth import authenticate


def inicio(request):
    context = {}
    return render(request,'index.html',context)
    
def informacion(request):
    context = {}
    return render(request,'informacion.pdf',context)

def recuperar(request):
    context = {}
    return render(request,'recuperar.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)

def editarActivos(request):
    context = {}
    return render(request,'editaractivos.html',context)

def logout_user(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['contrasena']

        # user = authenticate(request, username=correo, password=password)

    print(request.POST)
    return redirect('/logout/')

def error_404(request,exception):
    return page_not_found(request,'404.html')






