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
from .views import inicio, error_404, informacion
from .views import signout, recuperar


from django.contrib.auth import views as auth_views


# importe de imagenes
from django.conf import settings
from django.conf.urls.static import static

handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', signout, name='logout'),
    path('',auth_views.LoginView.as_view(), name='inicio'),
    path('inicio/', inicio, name="inicio-admin"),

    # Modulos de la aplicacion

    path('usuarios/', include('usuarios.urls')),
    path('novedades/', include('novedades.urls')),
    path('activos/', include('activos.urls')),
    path('informes/', include('informes.urls')),

    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),

    path('informacion/',informacion, name='informacion'),
    path('recuperar/',recuperar, name='recuperar'),
     
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
