"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from .views import inicio, login, informacion, recuperar, error_404


handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name='login'),
    path('inicio/', inicio, name="inicio"),
    path('usuarios/', include('usuarios.urls')),
    path('novedades/', include('novedades.urls')),
    path('activos/', include('activos.urls')),
    path('informes/', include('informes.urls')),
    path('configuracion/', include('configuracion.urls')),
    path('informacion/',informacion, name='informacion'),
    path('recuperar/',recuperar, name='recuperar'),  
]
