
from django.urls import path
from .views import activos


urlpatterns = [
    path('', activos, name='activos'),
]