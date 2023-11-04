from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from unicodedata import decimal

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
        'mueble': mueble,
        'promociones': Muebles_Oferta.objects.all()
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


def filtro_view(request):
    data = {
        'muebles': Mueble.objects.all(),
        'promociones': Muebles_Oferta.objects.all(),
        'title': 'Filtro de muebles',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'filtro.html', data)


@method_decorator(csrf_exempt)
def filtro(request):
    data = {}
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            precio_max = request.POST['precio']
            categoria = request.POST['categoria']

            consulta = Q()

            if nombre == '':
                pass
            else:
                consulta &= Q(nombre__icontains=nombre)
            if precio_max == 'Máximo':
                pass
            else:
                consulta &= Q(precio__lt=precio_max)
            if categoria == 'Todas':
                pass
            else:
                consulta &= Q(categoria__nombre__icontains=categoria)

            data = Mueble.objects.filter(consulta).values('nombre', 'categoria__nombre', 'precio', 'imagen', 'id')

        except Exception as e:
            data = {'error': str(e)}
    return JsonResponse(list(data), safe=False)
