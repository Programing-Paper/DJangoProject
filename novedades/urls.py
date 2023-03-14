
from django.urls import path
from .views import novedades, dtnovedades, Dtnovedades, editar_novedad

urlpatterns = [
    path('', novedades, name='novedades'), 
    path('', Dtnovedades.as_view(), name='novedad'),  
    path('data/',dtnovedades, name='datosnovedades'),
    path('editarnovedad/', editar_novedad, name='editarnovedades'),
    # path('crearcargo/', crearcargo, name='crearcargo'),
]