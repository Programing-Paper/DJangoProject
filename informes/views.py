from django.shortcuts import render
from multiprocessing import context

# Create your views here.


def informes(request):
    title= 'informes'
    context={
        'title': title
    }
    return render(request,'informes/informes.html', context)