from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')


def listado_parroquias(request):
    """
    """
    parroquias = Parroquia.objects.all()

    titulo = "Listado de Parroquias"
    informacion_template = {'parroquias': parroquias,
    'numero_parroquias': len(parroquias), 'mititulo': titulo}
    return render(request, 'listado_parroquias.html', informacion_template)

def listado_barrios(request):
    """
    """
    barrios = BarrioCiudadela.objects.all()

    titulo = "Listado de Barrios"
    informacion_template = {'barrios': barrios,
    'numero_barrios': len(barrios), 'mititulo': titulo}
    return render(request, 'listado_barrios.html', informacion_template)

def crear_parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(listado_parroquias)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_parroquia.html', diccionario)

def crear_barrio(request):
    """
    """
    if request.method=='POST':
        formulario = BarrioCiudadelaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(listado_barrios)
    else:
        formulario = BarrioCiudadelaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)