from src.views.funcionesHTML import *
from src.views.crearPaginaPorBicicleta import pagina_por_bicicleta
import sys
import os
"""
    Generando archivos .HTML empleando funciones del modulo html_generator
"""


# GENERANDO PAGINAS


def pagina_principal():
    sys.stdout = open('docs/home.html', 'w', encoding="UTF-8")
    html_head("Pagina principal - BookingBike",
              'Pagina de inicio de BookingBike')
    body.body_pagina_principal(nav)
    footer()
    sys.stdout.close()


def contacto():
    sys.stdout = open('docs/contacto.html', 'w', encoding="UTF-8")
    html_head(title="Pagina de contacto - BookingBike",
              description='Pagina de para contactar con la organización')
    body.body_contacto(nav)
    footer()
    sys.stdout.close()


def listado_total_bicis():
    sys.stdout = open('docs/listadototalbicis.html', 'w', encoding="UTF-8")
    html_head(title="Listado de bicis - BookingBike",
              description='Pagina que muestra todas las bicis disponibles')
    body.body_listado_total_bicis(nav)
    footer()
    sys.stdout.close()

def listado_tipo_bicis():
    sys.stdout = open('docs/listadotipobicis.html', 'w', encoding="UTF-8")
    html_head(title="Tipos de bicis disponibles - BookingBike",
              description='Pagina que muestra todos los tipos de bicis disponibles')
    body.body_listado_tipo_bicis(nav)
    footer()
    sys.stdout.close()

def listado_marca_bicis():
    sys.stdout = open('docs/listadomarcabicis.html', 'w', encoding="UTF-8")
    html_head(title="Marcas de bicis disponibles - BookingBike",
              description='Pagina que muestra todas las marcas de bicis disponibles')
    body.body_listado_marca_bicis(nav)
    footer()
    sys.stdout.close()

def listado_zona_bicis():
    sys.stdout = open('docs/listadobicisporzona.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por zona - BookingBike",
              description='Pagina que muestra todas las zonas que tienen bicis disponibles')
    body.body_listado_por_zona_bicis(nav)
    footer()
    sys.stdout.close()

def listado_tamaño_rueda_bicis():
    sys.stdout = open('docs/listadobicisportamañorueda.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por tamaño de rueda - BookingBike",
              description='Pagina que muestra todos los tamaño de rueda de bicis disponibles')
    body.body_listado_por_tamaño_rueda_bicis(nav)
    footer()
    sys.stdout.close()

def listado_desarollo_bicis():
    sys.stdout = open('docs/listadobicispordesarrollo.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por desarollo - BookingBike",
              description='Pagina que muestra todos los desarollos disponibles')
    body.body_listado_por_desarollo_bicis(nav)
    footer()
    sys.stdout.close()

def listado_cambios_bicis():
    sys.stdout = open('docs/listadobicisporcambio.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por tipo de cambio - BookingBike",
              description='Pagina que muestra todos los cambios disponibles')
    body.body_listado_por_cambio_bicis(nav)
    footer()
    sys.stdout.close()


def paginas_por_bicicletas():
    pagina_por_bicicleta(nav_2)

def listado_paginas_por_agrupaciones():
    paginas_tipos_bicis(nav_2)
    paginas_marcas_bicis(nav_2)
    paginas_zonas_bicis(nav_2)
    paginas_desarrollo_bicis(nav_2)
    paginas_tamaño_ruedas_bicis(nav_2)
    paginas_cambio_bicis(nav_2)
    

pagina_principal()
contacto()
listado_total_bicis()
listado_tipo_bicis()
listado_marca_bicis()
listado_zona_bicis()
listado_tamaño_rueda_bicis()
listado_desarollo_bicis()
listado_cambios_bicis()
paginas_por_bicicletas()
listado_paginas_por_agrupaciones()
