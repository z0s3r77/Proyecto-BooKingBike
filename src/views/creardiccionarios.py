from src.db.convertirJsonALista import bikes_json
from src.views.funcionesHTML import *
import sys


def diccionario_tipos_bicis():

    tipos_bicis = []


    def tiposBicis():
        x = 0
        while x <= (len(bikes_json)-1):

            tipo = bikes_json[x]['Model']['Name']
            if tipo in tipos_bicis:
                pass
            else:
                tipos_bicis.append(tipo)

            x += 1


    tiposBicis()



    diccionarioTiposBicis = {}


    for x in tipos_bicis:
        array = []
        for i in bikes_json:
            if x == i['Model']['Name']:
                array.append(i)
                diccionarioTiposBicis[x] = array
            
    return diccionarioTiposBicis


def diccionario_marcas_bicis():

    marcas_bicis = []


    def marcasBicis():
        x = 0
        while x <= (len(bikes_json)-1):

            tipo = bikes_json[x]['Brand']
            if tipo in marcas_bicis:
                pass
            else:
                marcas_bicis.append(tipo)

            x += 1


    marcasBicis()



    diccionarioMarcasBicis = {}


    for x in marcas_bicis:
        array = []
        for i in bikes_json:
            if x == i['Brand']:
                array.append(i)
                diccionarioMarcasBicis[x] = array
            
    return diccionarioMarcasBicis