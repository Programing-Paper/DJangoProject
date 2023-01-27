from django.shortcuts import render
from multiprocessing import context

# Create your views here.

def novedades(request):
    title= 'novedades'
    context={
        'title': title
    }
    return render(request,'novedades/novedades.html', context)