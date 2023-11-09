from django import forms
from django.contrib import admin

from Muebles.models import *


# Register your models here.


@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ['precio_minimo', 'precio_maximo']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_minimo', 'precio_maximo']
    form = CategoriaForm


@admin.register(Muebles_Oferta)
class Muebles_OfertaAdmin(admin.ModelAdmin):
    list_display = ['mueble', 'descuento']


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ['texto', 'imagen']