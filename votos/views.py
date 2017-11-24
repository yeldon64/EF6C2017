# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """

     #TODO TU CODIGO AQUI
    padron = 0
    for i in Distrito.objects.all():
        padron = padron+i.cantidad_votantes

    cant_votos = 0
    for i in Votos.objects.all():
        cant_votos += 1

    #cant_nulos = 0
    #for i in Votos.objects.all():
        #if i.voto == null:
            #cant_nulos += 1
    for a in Votos.objects.all():
        print (a)
        print (a.distrito)
        print (a.voto)

    #for can in Candidato.objects.all():
    #    for i in Votos.objects.all():
    #        if i.voto == can.nombre:


    context={}
    context['distritos'] = Distrito.objects.all()
    context['padron'] = padron
    context['porc_votantes'] = str((cant_votos*100)/padron) + "%"
    context['cant_votantes'] = (cant_votos)
    #context['cant_votantes_b'] = (cant_nulos)
   

    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    
    context={}

    #TODO TU CODIGO AQUI

    return render(request,'distrital.html',context)
