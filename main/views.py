from django.shortcuts import render
from django.views.defaults import page_not_found
# from django.contrib import messages
# from configuracion.models import Admin
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.contrib.auth import authenticate


def login(request):
    context = {}
    return render(request,'login.html',context)

def recuperar(request):
    context = {}
    return render(request,'recuperar.html',context)

def informacion(request):
    context = {}
    return render(request,'informacion.pdf',context)

def inicio(request):

    # usuario = Admin.objects.all()
    # if request.method == "POST":
    
    context = {}
    return render(request,'index.html',context)

def error_404(request, exception):
    return page_not_found(request, '404.html')






