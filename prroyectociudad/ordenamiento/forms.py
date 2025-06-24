from django.forms import models
from .models import Parroquia, BarrioCiudadela

class ParroquiaForm(models.Model):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo']

class BarrioCiudadelaForm(models.Model):
    class Meta:
        model = BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia']