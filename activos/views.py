from django.shortcuts import render, redirect
from multiprocessing import context
from activos.forms import ActivoForm
from activos.models import Activo
# from django.views import generic
# from django.http import JsonResponse
# from django.db.models import Q
# from django.views.generic import View


# Create your views here.

def activos(request):
    activos = Activo.objects.all()
    form = ActivoForm()
    if request.method == "POST":
        form = ActivoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("activos")
        else:
            form= ActivoForm()
            print("Error") 
    
    title= 'activo'
    context={
        'title': title,
        'activos': activos,
        'form': form
    }

    return render(request,'activos/activos.html', context)





