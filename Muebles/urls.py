from django.urls import path

from Muebles.views import inicio, muebles, mueble

app_name = 'Muebles'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('muebles/<int:id>/', muebles, name='muebles'),
    path('mueble/<int:id>/', mueble, name='mueble'),

]
