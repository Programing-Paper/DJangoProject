
from django.urls import path
from .views import activos


urlpatterns = [
    path('', activos, name='activos'),
    # path('', Dtserverside.as_view(), name='table'),   
    # path('serverside/',dt_serverside, name='datosactivos'),

]