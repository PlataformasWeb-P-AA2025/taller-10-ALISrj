from django.contrib import admin
from .models import *


# Register your models here.

class BarrioCiudadelaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero_parques',"numero_edificios","parroquia__nombre")
    list_filter = ('numero_parques',)
    search_fields = ('nombre', )

class BarrioCiudadelaInline(admin.StackedInline):
    model = BarrioCiudadela
    extra = 1

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','ubicacion','tipo')
    list_filter = ('tipo',)
    search_fields = ('nombre', )
    inlines = [BarrioCiudadelaInline,]

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(BarrioCiudadela, BarrioCiudadelaAdmin)