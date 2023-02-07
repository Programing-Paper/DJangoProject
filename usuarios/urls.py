
from django.urls import path
from .views import usuarios, dt_serverside, Dtserverside, editarusuario, crearcargo


urlpatterns = [
    path('', usuarios, name='usuarios'),
    path('', Dtserverside.as_view(), name='usuario'),   
    path('serverside/',dt_serverside, name='datosusuarios'),
    path('editarusuario/', editarusuario, name='editarusuario'),
    path('crearcargo/', crearcargo, name='crearcargo'),

]