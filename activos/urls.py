
from django.urls import path
from .views import activos, Dtserverside, dt_serverside, editaractivo

urlpatterns = [
    path('', activos, name='activos'),
    path('', Dtserverside.as_view(), name='activo'),
    path('serverside/',dt_serverside, name='datosactivos'),
    path('editaractivo/', editaractivo, name='editaractivos'),
    # path('crearcargo/', crearcargo, name='crearcargo'),
]