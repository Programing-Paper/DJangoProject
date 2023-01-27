from django.urls import path
from .views import config, formulario

urlpatterns = [
    path('', config, name='config'),
    path('formulario/', formulario, name='form'),

]
