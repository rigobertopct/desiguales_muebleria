from django.shortcuts import render

# Create your views here.
from Muebles.models import *


def inicio(request):
    if request.COOKIES.get('visited', False):
        visited = False
    else:
        visited = True
    data = {
        'title': 'Inicio',
        'categorias': Categoria.objects.all(),
        'promociones': Muebles_Oferta.objects.all(),
        'show_modal': visited
    }
    response = render(request, 'Inicio.html', data)
    response.set_cookie('visited', True)
    return response


def mueble(request, id):
    mueble = Mueble.objects.get(id=id)
    data = {
        'title': 'Mueble - ' + mueble.nombre,
        'mueble': mueble
    }
    return render(request, 'Mueble.html', data)

def muebles(request, id):
    categoria = Categoria.objects.get(id=id)
    muebles = Mueble.objects.filter(categoria_id=id)
    data = {
        'title': 'Categoría - ' + categoria.nombre,
        'muebles': muebles,
        'promociones': Muebles_Oferta.objects.all()
    }
    return render(request, 'muebles.html', data)