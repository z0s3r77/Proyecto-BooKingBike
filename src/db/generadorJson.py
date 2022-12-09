from src.db.conexionApiMongo import requestToMongoApi
import os
import json



def convertResponseStringIntoObjtect(response):

    #Damos el valor de la coleccion de bicicletas a response
    #Comprobamos que sea de tipo str

    try:
        assert isinstance(response,str)
    except:
        return False

    #Json.loads detecta en el string un formato JSON y lo convierte en un objeto Dict
    try:
        response = json.loads(response)
    except:
        return False


    return response




def generateJsonFileFromResponse(response, file):
    
    #Comprobamos si la respuesta es object Dict
    try:
        assert isinstance(response, dict)
    except:
        return False

    try:
        #Comprobamos si existe el directorio json , sino, lo crea
        if not os.path.exists('json/'):
            os.makedirs('json/')

        #Abrimos el archivo bikes.json con el fin de escribir en este "w"
        outFile = open(f"json/{file}.json", "w")

    except OSError:
        print("No se puede abrir el archivo")
        quit()
        
    else: 
            #json.dump nos permite convertir el diccionario en un objeto JSON
        json.dump(response["documents"], outFile, indent=4)
            
        outFile.close()

        return True


#Volcamos la respuesta de requestToMongoApi del modulo conexionApiMongo

def GeneradorJsonFile(response):

    response = convertResponseStringIntoObjtect(response)
    generateJsonFileFromResponse(response, "bikes")