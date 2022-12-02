import json
import os

def checkBikesJsonFile(path): 

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

def convertBikesJsonToList(path):
    json_file = open(path)
    json_file = json.load(json_file)
    
    return json_file



#Convertimos el JSON en una lista/diccionario python para poder tratarlo
def main(path):  

    #Comprueba que el archivo exista en ese path y que sea JSON
    checkBikesJsonFile(path)
    #Convierte el JSON en una lista llamada bikes_json
    bikes_json = convertBikesJsonToList(path)
    
    return bikes_json


bikes_json = main('json/bikes.json')
