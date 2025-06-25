from django.urls import path
# se importa las vistas de la aplicación
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('listado_parroquias/', listado_parroquias, name='listado_parroquias'),
    path('listado_barrios/', listado_barrios, name='listado_barrios'),
    path('crear_parroquia/', crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', crear_barrio, name='crear_barrio'),
]
