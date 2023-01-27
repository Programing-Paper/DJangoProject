from django.shortcuts import render, redirect
from configuracion.forms import AdminForm
from configuracion.models import Admin

# Create your views here.

def config(request):
    titulo="configuracion"
    form= AdminForm()
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
        else:
            print("Error")
    else:
        form= AdminForm()

    usuarios= Admin.objects.all()

    context = {
        'titulo':titulo,
        'form':form,
        'usuarios': usuarios
    }
    return render(request,'configuracion/config.html',context)

def formulario(request):
    titulo="formulario"
    context = {
        'titulo':titulo,
    }
    return render(request,'configuracion/form.html',context)