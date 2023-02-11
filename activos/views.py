from django.shortcuts import render, redirect
from multiprocessing import context
from activos.forms import ActivoForm, AsignarForm
from activos.models import Activo
from django.contrib import messages
from django.views import generic
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.


def activos(request):
    titulo = "Modulo activos"

    # formulario registrar activos

    activos = Activo.objects.all()
    asignar = AsignarForm()
    form = ActivoForm()
    if request.method == "POST":
        form = ActivoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("entro aqui")
            form.save()
            messages.success(
                request,f"Se agregó el activo {request.POST['idactivo']} exitosamente!"
            )
            return redirect('activo')
        else:
            messages.error(
                request,f"Error al agregar {request.POST['idactivo']}!"
            )
    else:
        form = ActivoForm()

    # formulario asignar activos

   
    context = {
        'titulo': titulo,
        'form': form,
        'activos': activos,
        'asignar': asignar
    }

    return render(request, 'activos/activos.html', context)

class Dtactivos(generic.TemplateView):
    template_name = 'activos'
    
def dt_activos(request):
    context= {}

    dt = request.GET

    draw = int(dt.get("draw"))
    start = int(dt.get("start"))
    length = int(dt.get("length"))
    search = dt.get("search[value]")


    registros = Activo.objects.all().order_by("idactivo")

    if search:
        registros = registros.filter(
                Q(idactivo__icontains=search) |
                Q(serial__icontains=search) |
                Q(so__icontains=search) |
                Q(marca__icontains=search) |
                Q(tipo__icontains=search) |
                Q(fecha__icontains=search) |
                Q(observaciones__icontains=search) |
                Q(situacion__icontains=search) |
                Q(empleadoid_id__icontains=search)    
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
            "idactivo" : d.idactivo,
            "serial" : d.serial,
            "so" : d.so,
            "marca" : d.marca,
            "tipo" : d.tipo,
            "fecha" : d.fecha,
            "observaciones" : d.observaciones,
            "situacion" : d.situacion,
            "empleadoid" : d.empleadoid_id,

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)

def editaractivo(request):
    title= 'Editar activo'
    # documento = Activo.objects.get(documento=cc)

    context={
        'title': title,
    }
    return render(request,'activos/editarActivos.html', context)

# def asignarActivo(request):
#     title= 'Editar activo'
#     # documento = Activo.objects.get(documento=cc)

#     context={
#         'title': title,
#     }
#     return render(request,'activos/editarActivos.html', context)




    







