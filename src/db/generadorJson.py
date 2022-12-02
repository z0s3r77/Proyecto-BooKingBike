from conexionApiMongo import requestToMongoApi
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

        #Abrimos el archivo bikes.json con el fin de escribir en este "w"
        outFile = open("JSON/bikes.json", "w")

    except OSError:
        print("No se puede abrir el archivo")
        SystemExit()
    
    else: 
        #json.dump nos permite convertir el diccionario en un objeto JSON
        json.dump(response["documents"], outFile, indent=4)
        
        outFile.close()


if __name__ == '__main__':

    #Volcamos la respuesta de requestToMongoApi del modulo conexionApiMongo
    response = requestToMongoApi()

    def mainGeneradorJson(response):

        response = convertResponseStringIntoObjtect(response)
        generateJsonFileFromResponse(response)
    
    mainGeneradorJson(response)