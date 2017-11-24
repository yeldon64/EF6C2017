# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Longitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    
    El modelo de candidato debe contar con un nombre para el candidato
    """
    nombre = models.CharField('Nombre del candidato', max_length=128)
    votantes = models.DecimalField('votos', max_digits = 100, decimal_places= 0, default= 0)
    def __str__(self):
        return 'Candidato {}'.format(self.nombre)
    


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Este modelo se eligio porque cada voto tiene que tener la informacion del candidato elegido (o voto en blanco) y el distrito del votante
    """
    voto = models.ForeignKey(Candidato, blank=True)
    distrito = models.ForeignKey(Distrito)


