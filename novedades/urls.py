
from django.urls import path
from .views import novedades, dtnovedades, Dtnovedades, editarnovedad



urlpatterns = [
    path('', novedades, name='novedades'), 
    path('', Dtnovedades.as_view(), name='novedad'),  
    path('data/',dtnovedades, name='datosnovedades'),
    path('editarnovedad/', editarnovedad, name='editarnovedades'),
    # path('crearcargo/', crearcargo, name='crearcargo'),
]