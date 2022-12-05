from src.views.funcionesHTML import *
import sys
"""
    Generando archivos .HTML empleando funciones del modulo html_generator
"""


# GENERANDO PAGINAS


def pagina_principal():
    sys.stdout = open('home.html', 'w', encoding="UTF-8")
    html_head(title="Pagina principal - BookingBike",
              description='Pagina de inicio de BookingBike')
    body.body_pagina_principal()
    footer()
    sys.stdout.close()


def contacto():
    sys.stdout = open('contacto.html', 'w', encoding="UTF-8")
    html_head(title="Pagina de contacto - BookingBike",
              description='Pagina de para contactar con la organización')
    body.body_contacto()
    footer()
    sys.stdout.close()


def listado_total_bicis():
    sys.stdout = open('listadototalbicis.html', 'w', encoding="UTF-8")
    html_head(title="Listado de bicis - BookingBike",
              description='Pagina que muestra todas las bicis disponibles')
    body.body_listado_total_bicis()
    footer()
    sys.stdout.close()

def listado_tipo_bicis():
    sys.stdout = open('listadotipobicis.html', 'w', encoding="UTF-8")
    html_head(title="Tipos de bicis disponibles - BookingBike",
              description='Pagina que muestra todos los tipos de bicis disponibles')
    body.body_listado_tipo_bicis()
    footer()
    sys.stdout.close()

def listado_marca_bicis():
    sys.stdout = open('listadomarcabicis.html', 'w', encoding="UTF-8")
    html_head(title="Marcas de bicis disponibles - BookingBike",
              description='Pagina que muestra todas las marcas de bicis disponibles')
    body.body_listado_marca_bicis()
    footer()
    sys.stdout.close()

def listado_zona_bicis():
    sys.stdout = open('listadobicisporzona.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por zona - BookingBike",
              description='Pagina que muestra todas las zonas que tienen bicis disponibles')
    body.body_listado_por_zona_bicis()
    footer()
    sys.stdout.close()


pagina_principal()
contacto()
listado_total_bicis()
listado_tipo_bicis()
listado_marca_bicis()
listado_zona_bicis()