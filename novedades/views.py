
from multiprocessing import context
from django.shortcuts import render, redirect
from novedades.models import Novedad
from django.contrib import messages
from novedades.forms import NovedadForm, UpdateForm
from django.views import generic
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required

# from django.views.defaults import exeption

# Create your views here.
# def hello(request):
#     return HTTPResponse('Hello word')

@login_required
def novedades(request):
    novedades = Novedad.objects.all()
    formnovedad = NovedadForm()
    if request.method == "POST" and 'formnovedad' in request.POST:
        print('entro aqui')
        formnovedad = NovedadForm(request.POST)
        if formnovedad.is_valid:
            print(request.POST)
            formnovedad.save()
            print('entro aqui')
            messages.success(
                request,f"Se agregó la novedad exitosamente!"
            )
            return redirect("novedad")
        else:
            messages.error(
                request,f"Error al agregar la novedad!"
            ) 
    else:
        formnovedad = NovedadForm()

    title= 'Informacion usuarios'
    context={
        'title': title,
        'novedades': novedades,
        'formnovedad': formnovedad,
    }
    return render(request,'novedades/novedades.html', context)

class Dtnovedades(generic.TemplateView):
    template_name = 'novedades'

@login_required
def dtnovedades(request):
    context= {}

    dt = request.GET

    draw = int(dt.get("draw"))
    start = int(dt.get("start"))
    length = int(dt.get("length"))
    search = dt.get("search[value]")


    registros = Novedad.objects.all().order_by("id")

    if search:
        registros = registros.filter(
                Q(id__icontains=search) |
                Q(fecha__icontains=search) |
                Q(empleado_id__icontains=search) |
                Q(estado__icontains=search) | 
                Q(activo_id__icontains=search) | 
                Q(descripcion__icontains=search)
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
            "id" : d.id,
            "descripcion" : d.descripcion,
            "fecha" : d.fecha,
            "empleado" : d.empleado_id,
            "estado" : d.estado,
            "activo" : d.activo_id,

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)

@login_required
def editar_novedad(request):
    titulo="Novedades - Editar"
    pk= request.GET.get('id')
    form_update=UpdateForm()
    novedad= Novedad.objects.get(id=pk)
    if request.method == "POST":
        print("Entro aqui")
        form_update= UpdateForm(request.POST, instance=novedad)
        if form_update.is_valid():
            form_update.save()
            messages.success(
                request,f"Se actualizo el novedad exitosamente!"
            )
            return redirect('novedad')       
        else:
            messages.success(
                request,f"ocurrio un error al guardar el novedad!"
            )
    else:
        form_update= UpdateForm(instance=novedad)


    context={
        'titulo':titulo,
        'form_update':form_update
    }
    return render(request,'novedades/editarNovedad.html',context)


# def editarnovedad(request):
#     title= 'Editar novedades'
#     # documento = Novedad.objects.get(documento=cc)

#     context={
#         'title': title,
#     }
#     return render(request,'novedades/editarNovedad.html', context)








    

