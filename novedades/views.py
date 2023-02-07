
from multiprocessing import context
from django.shortcuts import render, redirect
from novedades.models import Novedad
from django.contrib import messages
from novedades.forms import NovedadForm
from django.views import generic
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.views.defaults import exeption

# Create your views here.
# def hello(request):
#     return HTTPResponse('Hello word')


def novedades(request):
    usuarios = Novedad.objects.all()
    formnovedad = NovedadForm()
    if request.method == "POST":
        formnovedad = NovedadForm(request.POST)
        if formnovedad.is_valid:
            formnovedad.save()
            # messages.success(
            #     request,f"Se agregó la novedad exitosamente!"
            # )
            return redirect("novedad")
        else:
            messages.error(
                request,f"Error al agregar la novedad!"
            ) 
    else:
        formnovedad= NovedadForm()

    title= 'Informacion usuarios'
    context={
        'title': title,
        'usuarios': usuarios,
        'form': formnovedad,
    }
    return render(request,'novedades/novedades.html', context)

class Dtserverside(generic.TemplateView):
    template_name = 'novedades'

def dt_serverside(request):
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
                Q(empleadoid__icontains=search) |
                Q(estado__icontains=search) | 
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
            "empleadoid" : d.empleadoid,
            "estado" : d.estado,

        } for d in obj
    ]

    context["datos"] = datos
    return JsonResponse(context, safe=False)

def editarusuario(request):
    title= 'Editar novedades'
    # documento = Novedad.objects.get(documento=cc)

    context={
        'title': title,
    }
    return render(request,'novedades/editarNovedad.html', context)












    

