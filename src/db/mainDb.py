#Modulo principal de DB
from src.db.conexionApiMongo import requestToMongoApi
from src.db.generadorJson import GeneradorJsonFile
from src.db.convertirJsonALista import convertJsonToList


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


def getListfromJsonFile(rute):

    listResult =  convertJsonToList(rute)
    if type(listResult) == list:
        return listResult
    else:
        return False



def mainDB(rute,newjsonfile):
    
    if generateJsonFromResponseApi(newjsonfile) == True:
        listResult = getListfromJsonFile(rute)
        return listResult
    else:
        return False

