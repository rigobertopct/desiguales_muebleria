from django import template

from Muebles.models import Muebles_Oferta

register = template.Library()


@register.filter
def comprobar_promo(id):
    comprobar = False
    for item in Muebles_Oferta.objects.all():
        if item.mueble.id == id:
            comprobar = True
    return comprobar
