
from django.urls import path
from .views import usuarios, dt_serverside, Dtserverside, editar_empleados, crearcargo


urlpatterns = [
    path('', usuarios, name='usuarios'),
    path('', Dtserverside.as_view(), name='usuario'),   
    path('serverside/',dt_serverside, name='datosusuarios'),
    path('editarusuario/', editar_empleados, name='editarusuarios'),
    path('crearcargo/', crearcargo, name='crearcargo'),

]