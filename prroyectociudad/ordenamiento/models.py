from django.db import models


class Parroquia(models.Model):

    TIPO_CHOICES = [
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural'),
    ]

    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=300)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

class BarrioCiudadela(models.Model):

    NUMERO_PARQUES_CHOICES = [
        (1, '1 parque'),
        (2, '2 parques'),
        (3, '3 parques'),
        (4, '4 parques'),
        (5, '5 parques'),
        (6, '6 parques'),
    ]

    nombre = models.CharField(max_length=200)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=NUMERO_PARQUES_CHOICES)
    numero_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name='Parroquia', related_name='barrios')

