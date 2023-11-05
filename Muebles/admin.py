from django.contrib import admin

# Register your models here.
from Muebles.models import *


@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'imagen']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_minimo', 'precio_maximo']


@admin.register(Muebles_Oferta)
class Muebles_OfertaAdmin(admin.ModelAdmin):
    list_display = ['mueble', 'descuento']


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ['texto', 'imagen']