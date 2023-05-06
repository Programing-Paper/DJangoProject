from django.shortcuts import render, redirect
from activos.forms import ActivoForm, UpdateForm, AsignarForm
from activos.models import Activo
from django.contrib import messages
from django.views import generic
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.

@login_required(login_url='inicio')


@login_required
@permission_required('activos.view_activo')
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

    formasignar = AsignarForm()

    if request.method == 'POST':
            activo = Activo.objects.filter(idactivo = int(request.POST['id'])).update(
                empleado_id= request.POST['empleado']
            )
            messages.success(
                request,f"Se asigno el activo exitosamente!"
            )
            return redirect('activo')
    else:
        print('hola')
   
    context = {
        'titulo': titulo,
        'form': form,
        'activos': activos,
        'asignar': formasignar

    }

    return render(request, 'activos/activos.html', context)

class Dtactivos(generic.TemplateView):
    template_name = 'activo'
    
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
                Q(empleado_id__icontains=search)    
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


    # datos= []
    # for d in obj:
    #     datos.append({
    #         "idactivo" : d.idactivo,
    #         "serial" : d.serial,
    #         "so" : d.so,
    #         "marca" : d.marca,
    #         "tipo" : d.tipo,
    #         "fecha" : d.fecha,
    #         "observaciones" : d.observaciones,
    #         "situacion" : d.situacion,
    #         "empleadoid" : d.idempleado,
    #     })

    # activos = Activo.objects.all()

    # for activo in activos:
    #     yield activo.empleado
   
    datos = []
    for item in obj:
        datos.append({
            'idactivo': item.idactivo,
            'serial': item.serial,
            'marca': item.marca,
            'tipo': item.tipo,
            'fecha': item.fecha,
            'observaciones': item.observaciones,
            'situacion': item.situacion,
            'empleado': item.empleado.nombres,
        })

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





    







