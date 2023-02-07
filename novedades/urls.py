
from django.urls import path
from .views import novedades, Dtserverside, dt_serverside, editarusuario



urlpatterns = [
    path('', novedades, name='novedades'),
    path('', Dtserverside.as_view(), name='novedad'),   
    path('serverside/',dt_serverside, name='datosnovedades'),
    path('editarusuario/', editarusuario, name='editarnovedades'),
    # path('crearcargo/', crearcargo, name='crearcargo'),
]