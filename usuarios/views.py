# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from usuarios.models import Empleado, Cargo
from django.contrib import messages
from usuarios.forms import EmpleadoForm, CargoForm, UpdateForm
from django.views import generic
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.views.defaults import exeption

# Create your views here.
# def hello(request):
#     return HTTPResponse('Hello word')


def usuarios(request):
    usuarios = Empleado.objects.all()
    form = EmpleadoForm()
    if request.method == "POST":
        print("entro aqui")
        form = EmpleadoForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(
                request,f"Se agregó el usuario {request.POST['nombres']} exitosamente!"
            )
            return redirect("usuario")
        else:
            messages.error(
                request,f"Error al agregar {request.POST['nombres']}!"
            ) 
    else:
        form= EmpleadoForm()

    title= 'Informacion usuarios'
    context={
        'title': title,
        'usuarios': usuarios,
        'form': form,
    }
    return render(request,'usuarios/usuarios.html', context)

class Dtserverside(generic.TemplateView):
    template_name = 'usuarios'

def dt_serverside(request):
    context= {}

    dt = request.GET

    draw = int(dt.get("draw"))
    start = int(dt.get("start"))
    length = int(dt.get("length"))
    search = dt.get("search[value]")


    registros = Empleado.objects.all().order_by("documento")

    if search:
        registros = registros.filter(
                Q(documento__icontains=search) |
                Q(nombres__icontains=search) |
                Q(apellidos__icontains=search) |
                Q(compania__icontains=search) |
                Q(estado__icontains=search) |
                Q(telefono__icontains=search) |
                Q(direccion__icontains=search) 
        )
    
    recordsTotal = registros.count()
    recordsFiltered = recordsTotal

    # preparando la salida 

    context['draw'] = draw
    context['recordsTotal'] = recordsTotal
    context['recordsFiltered'] = recordsFiltered

    reg = registros[start:start + length]
    paginator = Paginator(reg,length)

    try:
        obj = paginator.page(draw).object_list
    except PageNotAnInteger:
        obj = paginator.page(draw).object_list
    except EmptyPage:
        obj = paginator.page(paginator.num_pages).object_list

    datos = [
        {
            "documento" : d.documento,
            "nombres" : d.nombres,
            "apellidos" : d.apellidos,
            "compania" : d.compania,
            "estado" : d.estado,
            "telefono" : d.telefono,
            "direccion" : d.direccion,
            # "opciones" : (f"<a href='' ><i class='bi bi-pencil-square'></i></a>"),

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)

def crearcargo(request):
    cargos = Cargo.objects.all()
    cargoform = CargoForm()
    if request.method == "POST":
        print("entro aqui")
        cargoform = CargoForm(request.POST)
        if cargoform.is_valid:
            cargoform.save()
            return redirect("crearcargo")
        else:
            cargoform= CargoForm()
            print("Error")

    title= 'Agregar cargos'
    context={
        'title': title,
        'cargoform': cargoform,
        'cargos': cargos
    }
    return render(request,'usuarios/crearcargos.html', context)



def editar_empleados(request):
    titulo="Usuarios - Editar"
    pk= request.GET.get('id')
    form_update=UpdateForm()
    usuario= Empleado.objects.get(documento=pk)
    if request.method == "POST":
        print("Entro aqui")
        form_update= UpdateForm(request.POST, instance=usuario)
        if form_update.is_valid():
            form_update.save()
            messages.success(
                request,f"Se actualizo el usuario {request.POST['nombres']} exitosamente!"
            )
            return redirect('usuario')
        else:
            messages.error(
                request,f"ocurrio un error al actualizar el usuario {request.POST['nombres']}!"
            )
    else:
        form_update= UpdateForm(instance=usuario)

    context={
        'titulo':titulo,
        'form_update':form_update
    }
    return render(request,'usuarios/editarUsuario.html',context)


# def editarusuario(request):
#     title= 'Editar usuario'
#     # documento = Empleado.objects.get(documento=cc)

#     context={
#         'title': title,
#     }
#     return render(request,'usuarios/editarUsuario.html', context)



    

