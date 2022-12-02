import json
import jsonschema
from jsonschema import validate
import os

def checkBikesJson(path): 

    #Comprobamos que el JSON exista en el path
    isExist = os.path.exists(path)

    if isExist == True:
        print(f"El JSON existe en este path: {path}")
    else:
        print(f'El JSON no se encuentra en este path: {path}')


    #Comprobamos que el JSON es un JSON verdadero 
    with open(path) as json_file:
        try:
            json.load(json_file)
            print(f"El fichero es efectivamente un JSON")

        except ValueError:
            print('El fichero no es un json')

#Convertimos el JSON en una lista

def jsonToList(path):
    json_file = open(path)
    json_file = json.load(json_file)
    
    return json_file

#Comprobamos que se haya convertido en lista correctamente

def checkEstructuraBikesJson(bikes_json): 

    assert isinstance(bikes_json, list)



#Convertimos el JSON en una lista/diccionario python para poder tratarlo

def main(path):  

    #Comprueba que el archivo exista en ese path y que sea JSON
    checkBikesJson(path)
    #Convierte el JSON en una lista llamada bikes_json
    bikes_json = jsonToList(path)
    
    return bikes_json


bikes_json = main('json/bikes.json')
