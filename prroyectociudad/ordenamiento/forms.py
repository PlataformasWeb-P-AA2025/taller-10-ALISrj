from django.forms import ModelForm
from .models import Parroquia, BarrioCiudadela


class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']


class BarrioCiudadelaForm(ModelForm):
    class Meta:
        model = BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia']
