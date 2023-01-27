
from django.urls import path

from novedades.views import novedades



urlpatterns = [
    path('', novedades, name='novedades')
]