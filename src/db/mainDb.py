#Modulo principal de DB
from conexionApiMongo import requestToMongoApi
from generadorJson import GeneradorJsonFile
from convertirJsonALista import convertJsonToList


#Funcion Principal
def mainDb(): 

    #Obtenemos la respuesta de la API
    response = requestToMongoApi()

    #Generamos un archivo JSON a partir de la respuesta
    GeneradorJsonFile(response)

    #Obtenemos la lista de documentos a partir del archivo JSON
    bikesList = convertJsonToList('json/bikes.json')

    #Devolvemos una lista con los documentos de la colección de Bicicletas
    return bikesList

