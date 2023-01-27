# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render

# from django.views.defaults import exeption



# Create your views here.
# def hello(request):
#     return HTTPResponse('Hello word')

def usuarios(request):
    title= 'usuarios'
    context={
        'title': title
    }
    return render(request,'usuarios/usuarios.html', context)


