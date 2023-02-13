
from django.urls import path
from .views import activos, Dtactivos, dt_activos, editar_activo

urlpatterns = [
    path('', activos, name='activos'),
    path('', Dtactivos.as_view(), name='activo'),
    path('server/',dt_activos, name='datosactivos'),
    path('editaractivo/', editar_activo, name='editaractivos'),
]