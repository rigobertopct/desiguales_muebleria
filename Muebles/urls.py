from django.urls import path

from Muebles.views import *

app_name = 'Muebles'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('muebles/<int:id>/', muebles, name='muebles'),
    path('mueble/<int:id>/', mueble, name='mueble'),
    path('filtro/', filtro_view, name='filtro'),
    path('filtro_view/', filtro, name='filtro_view'),

]
