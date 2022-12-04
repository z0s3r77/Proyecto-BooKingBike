from conexionApiMongo import requestToMongoApi
import os
import json



def convertResponseStringIntoObjtect(response):

    #Damos el valor de la coleccion de bicicletas a response
    #Comprobamos que sea de tipo str
    # response = requestToMongoApi()
    assert isinstance(response,str)

    #Json.loads detecta en el string un formato JSON y lo convierte en un objeto Dict
    response = json.loads(response)

    return response




def generateJsonFileFromResponse(response):
    
    #Check response es object Dict
    assert isinstance(response, dict)

    try:
        #Comprobamos si existe el directorio json <> lo crea
        if not os.path.exists('json/'):
            os.makedirs('json/')

        #Abrimos el archivo bikes.json con el fin de escribir en este "w"
        outFile = open("json/bikes.json", "w")

    except OSError:
        print("No se puede abrir el archivo")
        quit()
    
    else: 
        #json.dump nos permite convertir el diccionario en un objeto JSON
        json.dump(response["documents"], outFile, indent=4)
        
        outFile.close()



#Volcamos la respuesta de requestToMongoApi del modulo conexionApiMongo

def GeneradorJsonFile(response):

    response = convertResponseStringIntoObjtect(response)
    generateJsonFileFromResponse(response)