from django.shortcuts import render, redirect
from multiprocessing import context
from activos.forms import ActivoForm
from activos.models import Activo
# from django.views import generic
# from django.http import JsonResponse
# from django.db.models import Q
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import View


# Create your views here.

def activos(request):

    # activos = Activo.objects.all()
    # form = ActivoForm()

    # if request.method == "GET":
    #     print('entro aqui al get')
    #     return render(request, 'activos', {
    #         'form' : ActivoForm()
    #     })
    # else:
    #     form = ActivoForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid:
    #         form.save()
    #         print('se registro el activo correctamente')
    #         return redirect("activos")
    #     else:
    #         form= ActivoForm()
    #         print("Error")
    
    # title= 'activo'
    # context={
    #     'title': title,
    #     'activos': activos,
    #     'form': form
    # }

    # print('entra aqui')

    # return render(request,'activos/activos.html', context)

    titulo = "Modulo activos"
    form = ActivoForm()
    if request.method == "POST":
        form = ActivoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('entro aqui')
            return redirect('activos')
        else:
            print("Error")
    else:
        form = ActivoForm()

    activos = Activo.objects.all()

    context = {
        'titulo': titulo,
        'form': form,
        'activos': activos,
    }

    return render(request, 'activos/activos.html', context)






    







