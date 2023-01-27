from django.shortcuts import render, redirect
from multiprocessing import context
from activos.forms import ActivoForm
from activos.models import Activo

# Create your views here.

def activos(request):
    activos = Activo.objects.all()
    title= 'activo'
    context={
        'title': title
    }
    return render(request,'activos/activos.html', {"activos": activos })

def insertarDatos(request):
    # print(request.POST['marca'])
    activos = Activo(marca=request.POST['fecha'], idactivo=request.POST['idactivo'])
    activos.save()
    return redirect('/activos/')


def editarActivos(request):
    title= 'Editar activos'
    context={
        'title': title
    }
    return render(request,'editaractivos.html', context)

def deleteActivo(request, idactivo):
    delete = Activo.objects.get(id=idactivo)
    delete.delete()
    title= 'Editar activos'
    context={
        'title': title
    }
    return redirect('/activos/')

def registrarActivos(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            print("El activo se registro correctamente")
            return redirect('activos')
        else:
            print("El Activo no se registro!")
    else:
        form= ActivoForm()
    context={
        'form': form
    }
    # return render(request,'editaractivos.html', context)
