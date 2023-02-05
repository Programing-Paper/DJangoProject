# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from usuarios.models import Empleado
from usuarios.forms import EmpleadoForm
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
            return redirect("usuario")
        else:
            form= EmpleadoForm()
            print("Error") 

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

    url= "editarusuario"
    datos = [
        {
            "documento" : d.documento,
            "nombres" : d.nombres,
            "apellidos" : d.apellidos,
            "compania" : d.compania,
            "estado" : d.estado,
            "telefono" : d.telefono,
            "direccion" : d.direccion,
            "opciones" : (f"<a href={url} ><i class='bi bi-pencil-square'></i></a>"),

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)

def editarusuario(request, cc):
    title= 'Editar usuario'
    documento = Empleado.objects.get(documento=cc)
    

    context={
        'title': title,
    }
    return render(request,'usuarios/editarUsuario.html', context)










    

