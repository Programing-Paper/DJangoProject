from django.urls import path
from .views import config, formulario, deleteAdmin, cambiar

urlpatterns = [
    path('', config, name='config'),
    path('formulario/', formulario, name='form'),
    path('eliminar/<int:idadmin>/', deleteAdmin, name='delete'),
    path('cambiar-estado/<int:cambiar>/', cambiar, name='cambiarestado'),
]
