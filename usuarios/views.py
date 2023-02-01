# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from usuarios.models import Empleado
from usuarios.forms import EmpleadoForm

# from django.views.defaults import exeption

# Create your views here.
# def hello(request):
#     return HTTPResponse('Hello word')

def usuarios(request):
    usuarios = Empleado.objects.all()
    form = EmpleadoForm()
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("usuarios")
        else:
            form= EmpleadoForm()
            print("Error") 


    title= 'usuarios'
    context={
        'title': title,
        'usuarios': usuarios,
        'form': form

    }
    return render(request,'usuarios/usuarios.html', context)


