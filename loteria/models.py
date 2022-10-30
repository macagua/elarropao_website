# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
#from elarropao.loteria.widgets import ColorPickerWidget
from elarropao.loteria.fields import ColorField

CONTENEDOR = (
    (1, 'Derecho'),
    (2, 'Izquierdo')
)

ORDEN = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
)

TIPO_PUBLICIDAD = (
    (1, 'Flash'),
    (2, 'Imagen'),
)

TIPO_SORTEO = (
    (1, 'Triples'),
    (2, 'Kino'),
    (3, 'Triple Gordo'),
    (4, 'Papaya'),
)

NUMEROS_TRIPLE = [('%03d' % i, '%03d' % i) for i in range(1000)]
NUMEROS_TERMINAL = [('%02d' % i, '%02d' % i) for i in range(100)]

COLORES = (
    ('aqua', 'Celeste'),
    ('black', 'Negro'),
    ('blue', 'Azul'),
    ('fuchsia', 'Fucsia'),
    ('gray', 'Gris'),
    ('green', 'Verde'),
    ('lime', 'Lima'),
    ('maroon', 'Marron'),
    ('navy', 'Azul marino'),
    ('olive', 'Oliva'),
    ('purple', 'Morado'),
    ('red', 'Rojo'),
    ('silver', 'Platiado'),
    ('teal', 'Verde Azulado'),
    ('white', 'Blanco'),
    ('yellow', 'Amarillo'),
)


class CampoColor(models.Model):
    color = ColorField(blank=True)

    def __unicode__(self):
        return str(self.color)   
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"


class Loteria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='loteria')

    def __unicode__(self):
        return self.nombre.encode('ascii', 'replace')
    
    class Meta:
        verbose_name = "Loteria"
        verbose_name_plural = "Loterias"
        ordering = ['nombre']
    
class Sorteo(models.Model):
    nombre = models.CharField(max_length=50)
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    hora = models.TimeField()
    tipo = models.IntegerField(choices=TIPO_SORTEO, verbose_name='Tipo de Sorteo')
    loteria = models.ForeignKey(Loteria)
    
    def __unicode__(self):
        return "%s - %s" %  (self.loteria, self.nombre.encode('ascii', 'replace'))
#        return self.nombre.encode('ascii', 'replace')
    
    class Meta:
        verbose_name = "Sorteo"
        verbose_name_plural = "Sorteos"
        ordering = ['loteria','hora','nombre']
    
class Animalito(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='loteria')
    
    def __unicode__(self):
        return self.nombre.encode('ascii', 'replace')
    
    class Meta:
        verbose_name = "Animalito"
        verbose_name_plural = "Animalitos"
        ordering = ['nombre']

class Signo(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='loteria')

    def __unicode__(self):
        return self.nombre.encode('ascii', 'replace')
    
    class Meta:
        verbose_name = "Signo"
        verbose_name_plural = "Signos"
        ordering = ['nombre']
    
class Resultado_Triple(models.Model):
    numero = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    animalito = models.ForeignKey(Animalito)
    signo = models.ForeignKey(Signo)
    sorteo = models.ForeignKey(Sorteo)
    fecha = models.DateField()
    
    def __unicode__(self):
        return self.numero
    
    class Meta:
        verbose_name = "Resultado Triple"
        verbose_name_plural = "Resultados Triple"
        order_with_respect_to = 'sorteo'

class Resultado_Kino(models.Model):
    numero_sorteo = models.IntegerField()
    numero1 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero2 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero3 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero4 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero5 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero6 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero7 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero8 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero9 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero10 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero11 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero12 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero13 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero14 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    numero15 = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    sorteo = models.ForeignKey(Sorteo)
    fecha = models.DateField()

    def __unicode__(self):
        return str(self.numero_sorteo)    
    
    class Meta:
        verbose_name = "Resultado Kino"
        verbose_name_plural = "Resultados Kino"
        
class Resultado_Triple_Gordo(models.Model):
    numero_sorteo = models.IntegerField()
    color = models.CharField(max_length=100)
    super_dupleta_1 = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    super_dupleta_2 = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    super_dupleta_3 = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    especial_cantado = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    par_millonario_a = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    par_millonario_b = models.CharField(max_length=3, choices=NUMEROS_TRIPLE)
    sorteo = models.ForeignKey(Sorteo)
    fecha = models.DateField()

    def __unicode__(self):
        return str(self.numero_sorteo)   
    
    class Meta:
        verbose_name = "Resultado Triple Gordo"
        verbose_name_plural = "Resultados Triple Gordo"
        
class Resultado_Papaya(models.Model):
    numero_sorteo = models.IntegerField()
    triple_terminal_a = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    triple_terminal_b = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    triple_terminal_c = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_a_a = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_a_b = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_b_a = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_b_b = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_c_a = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    doblete_c_b = models.CharField(max_length=2, choices=NUMEROS_TERMINAL)
    sencillo = models.CharField(max_length=10)
    sorteo = models.ForeignKey(Sorteo)
    fecha = models.DateField()

    def __unicode__(self):
        return str(self.numero_sorteo)    
    
    class Meta:
        verbose_name = "Resultado Papaya"
        verbose_name_plural = "Resultados Papaya"
        
class Publicidad(models.Model):
    archivo = models.FileField(upload_to='publicidad')
    tipo = models.IntegerField(choices=TIPO_PUBLICIDAD, verbose_name='Tipo de Archivo')
    contenedor = models.IntegerField(choices=CONTENEDOR)
    orden = models.IntegerField(choices=ORDEN)
    
    class Meta:
        verbose_name = "Publicidad"
        verbose_name_plural = "Publicidades"

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    nota = models.TextField()
    publicar = models.BooleanField()

    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

# Extendiendo emencia.django.newsletter
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)

    def __unicode__(self):
        return str(self.email)    
    
    class Meta:
        verbose_name = "Perfil de lista de correos"
        verbose_name_plural = "Perfiles de lista de correos"

# Extendiendo las flatpages
from django.contrib.flatpages.models import FlatPage

def publicidad_derecha(self):
    from elarropao.loteria.models import Publicidad
    publicidad_derecha = Publicidad.objects.filter(contenedor=1).order_by('orden')
    return publicidad_derecha

FlatPage.add_to_class('publicidad_derecha', publicidad_derecha)

def publicidad_izquierda(self):
    from elarropao.loteria.models import Publicidad
    publicidad_izquierda = Publicidad.objects.filter(contenedor=2).order_by('orden')
    return publicidad_izquierda

FlatPage.add_to_class('publicidad_izquierda', publicidad_izquierda)

