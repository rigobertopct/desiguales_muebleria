from django.db import models

# Create your models here.
#
from django.db.models import CASCADE


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    precio_minimo = models.DecimalField(decimal_places=2, max_digits=10)
    precio_maximo = models.DecimalField(decimal_places=2, max_digits=10)
    imagen = models.ImageField(upload_to='categorias', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Mueble(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='categorias', blank=True, null=True)

    class Meta:
        verbose_name = 'Mueble'
        verbose_name_plural = 'Muebles'

    def __str__(self):
        return self.nombre


class Muebles_Oferta(models.Model):
    mueble = models.ForeignKey(Mueble, on_delete=CASCADE)
    descuento = models.DecimalField(decimal_places=2, max_digits=6)

    def calcular_precio(self):
        resultado=self.mueble.precio * self.descuento / 100
        return round(resultado, 2)

    class Meta:
        verbose_name = 'Mueble en Oferta'
        verbose_name_plural = 'Muebles en Oferta'


class Promocion(models.Model):
    imagen = models.ImageField(upload_to='promocion')
    texto = models.TextField()

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'
