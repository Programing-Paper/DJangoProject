from django.shortcuts import render, redirect
from configuracion.forms import AdminForm, UpdateProfile
from configuracion.models import Admin

# Create your views here.


def config(request):
    titulo = "configuracion"
    form = AdminForm()
    if request.method == "POST":
        form = AdminForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('config')
        else:
            print("Error")
    else:
        form = AdminForm()

    usuarios = Admin.objects.all()

    context = {
        'titulo': titulo,
        'form': form,
        'usuarios': usuarios,
        'update': UpdateProfile
    }
    return render(request, 'configuracion/config.html', context)


def formulario(request):
    titulo = "formulario"
    context = {
        'titulo': titulo,
    }
    return render(request, 'configuracion/form.html', context)


def deleteAdmin(request, idadmin):
    delete = Admin.objects.get(id=idadmin)
    delete.delete()
    message= 'El usuario se elimino correctamente'
    return redirect('config')

    title = 'delete'
    context = {
        'title': title,
        'message': message
    }
    return render(request, 'configuracion/config.html', context)


def cambiar(request, cambiar):
    estado= Admin.objects.all()
    Admin.objects.filter(userestado=cambiar).update(
        userestado='0'
    )
    return redirect('config')

    title = 'Estado'
    context = {
        'title': title,
        'estado': estado
    }
    return render(request, 'configuracion/config.html', context)

    
