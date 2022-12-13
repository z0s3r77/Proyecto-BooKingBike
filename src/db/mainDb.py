#Modulo principal de DB
from src.db.conexionApiMongo import requestToMongoApi
from src.db.generadorJson import GeneradorJsonFile
from src.db.convertirJsonALista import convertJsonToList



#Esta funcion pide un nombre como parametro, 
#Este nombre es el que su utilizará para crear el archivo en json/
def generateJsonFromResponseApi(newjsonfile):

    response = requestToMongoApi()

    if type(response) == str:

        try:
            if GeneradorJsonFile(response, newjsonfile) == False:
                return False
        except:
            return False
        else:
            return True



#La siguiente función  crea un array con los documentos 
#Del archivo JSON creado anteriormente
def getListfromJsonFile(rute):

    listResult =  convertJsonToList(rute)
    if type(listResult) == list:
        return listResult
    else:
        return False



#MainDB une las dos funciones anteriores y devuelve un array con los documentos.
#Dichos documentos son el resultado del RESPONSE a la API de MONGO ATLAS.
#Este response se convierte en fichero JSON y de ahí se pasan los datos a una lista.
def mainDB(rute,newjsonfile):
    
    if generateJsonFromResponseApi(newjsonfile) == True:
        listResult = getListfromJsonFile(rute)
        return listResult
    else:
        return False

