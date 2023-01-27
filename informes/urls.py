
from django.urls import path

from informes.views import informes

urlpatterns = [
    path('', informes, name='informes')
]