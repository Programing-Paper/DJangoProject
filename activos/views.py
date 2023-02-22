from django.shortcuts import render, redirect
from multiprocessing import context
from activos.forms import ActivoForm, UpdateForm, AsignarForm
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
    form = ActivoForm()
    if request.method == "POST" and 'crearform' in request.POST:
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
    formasignar = AsignarForm()

    if request.method == "POST" and 'asignarform' in request.POST:
        formasignar = AsignarForm(request.POST)
        print(request.POST)
        if formasignar.is_valid():
            print("entro aqui")
            formasignar.save()
            messages.success(
                request,f"Se asigno el activo a el exitosamente!"
            )
            return redirect('activo')
        else:
            messages.error(
                request,f"Error al asignar el empleado exitosamente!"
            )
    else:
        formasignar = AsignarForm()
   
    context = {
        'titulo': titulo,
        'form': form,
        'activos': activos,
        'asignar': formasignar

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
                Q(idempleado_id__icontains=search)    
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
            "empleadoid" : d.idempleado_id,

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)


def editar_activo(request):
    titulo="Activos - Editar"
    pk= request.GET.get('id')
    form_update=UpdateForm()
    activo= Activo.objects.get(idactivo=pk)
    if request.method == "POST":
        print("Entro aqui")
        form_update= UpdateForm(request.POST, instance=activo)
        if form_update.is_valid():
            form_update.save()
            messages.success(
                request,f"Se actualizo el activo {request.POST['marca']} exitosamente!"
            )
            return redirect('activo')
        else:
            messages.error(
                request,f"ocurrio un error al guardar el activo {request.POST['marca']}!"
            )
    else:
        form_update= UpdateForm(instance=activo)


    context={
        'titulo':titulo,
        'form_update':form_update
    }
    return render(request,'activos/editarActivos.html',context)




    







