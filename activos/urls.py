
from django.urls import path
from .views import activos, editarActivos, insertarDatos, deleteActivo

urlpatterns = [
    path('', activos, name='activos'),
    path('editar/', editarActivos),
    path('insertar/', insertarDatos, name='insertar'),
    path('delete-activo/<int:idactivo>/', deleteActivo, name='delete-activo'),
]