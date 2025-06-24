from django.urls import path
# se importa las vistas de la aplicación
from .views import *

urlpatterns = [
    path('listado_parroquias/', listado_parroquias, name='listado_parroquias'),
    path('listado_barrios/', listado_barrios, name='listado_barrios'),

    # path('detalle/matricula/<int:id>', views.detalle_matricula,
    #     name='detalle_matricula'),
    # path('crear/nueva/matricula', views.crear_matricula,
    #     name='crear_matricula'),
    # path('editar/matricula/<int:id>', views.editar_matricula,
    #         name='editar_matricula'),
    # path('detalle/estudiante/<int:id>', views.detalle_estudiante,
    #     name='detalle_estudiante'),

]
