from src.db.convertirJsonALista import convertJsonToList
# from src.views.funcionesHTML import *
import sys

bikes_json = convertJsonToList('json/bikes.json')

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

            marca = bikes_json[x]['Brand']
            if marca in marcas_bicis:
                pass
            else:
                marcas_bicis.append(marca)

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

def diccionario_zonas_bicis():

    zonas_bicis = []


    def zonasBicis():
        x = 0
        while x <= (len(bikes_json)-1):

            zona = bikes_json[x]['Location']
            if zona in zonas_bicis:
                pass
            else:
                zonas_bicis.append(zona)

            x += 1


    zonasBicis()



    diccionarioZonasBicis = {}


    for x in zonas_bicis:
        array = []
        for i in bikes_json:
            if x == i['Location']:
                array.append(i)
                diccionarioZonasBicis[x] = array
            
    return diccionarioZonasBicis



def diccionario_tamaño_ruedas_bicis():

    tamaño_ruedas_bicis = []


    def tamaño_Ruedas_Bicis():
        x = 0
        while x <= (len(bikes_json)-1):

            tamaño_rueda = bikes_json[x]['Model']['Wheel size']['$numberDouble']
            if tamaño_rueda in tamaño_ruedas_bicis:
                pass
            else:
                tamaño_ruedas_bicis.append(tamaño_rueda)

            x += 1


    tamaño_Ruedas_Bicis()



    diccionarioTamañoRuedasBicis = {}


    for x in tamaño_ruedas_bicis:
        array = []
        for i in bikes_json:
            if x == i['Model']['Wheel size']['$numberDouble']:
                array.append(i)
                diccionarioTamañoRuedasBicis[x] = array
            
    return diccionarioTamañoRuedasBicis


def diccionario_desarrollo_bicis():

    desarrollo_bicis = []


    def desarrolloBicis():
        x = 0
        while x <= (len(bikes_json)-1):

            desarrollo = bikes_json[x]['Model']['Developments']
            if desarrollo in desarrollo_bicis:
                pass
            else:
                desarrollo_bicis.append(desarrollo)

            x += 1


    desarrolloBicis()



    diccionarioDesarrolloBicis = {}


    for x in desarrollo_bicis:
        array = []
        for i in bikes_json:
            if x == i['Model']['Developments']:
                array.append(i)
                diccionarioDesarrolloBicis[x] = array
            
    return diccionarioDesarrolloBicis


def diccionario_cambios_bicis():

    cambios_bicis = []


    def cambioBicis():
        x = 0
        while x <= (len(bikes_json)-1):

            cambios = bikes_json[x]['Model']['Type']
            if cambios in cambios_bicis:
                pass
            else:
                cambios_bicis.append(cambios)

            x += 1


    cambioBicis()



    diccionarioCambiosBicis = {}


    for x in cambios_bicis:
        array = []
        for i in bikes_json:
            if x == i['Model']['Type']:
                array.append(i)
                diccionarioCambiosBicis[x] = array
            
    return diccionarioCambiosBicis