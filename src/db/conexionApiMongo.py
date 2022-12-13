import requests
from src.db.MongoAtlasConexion import MongoKey
import json

# Creamos una función que nos permite hacer una petición de datos a MongoAtlas
# En esta petición(request) obtenemos como respuesta la colección de bikes

def requestToMongoApi():
  
  #Datos necesarios para hacer el request a la API de MongoAtlas
  url = "https://data.mongodb-api.com/app/data-cozpc/endpoint/data/v1/action/find"
  payload = json.dumps({
      "collection": "bikes",
      "database": "BookingBike",
      "dataSource": "Sandbox",
      "projection":{
        "_id":1,
        "Brand":1,
        "Model":1,
        "Price":1,
        "Status":1,
        "Location":1,
        "img":1
        }
  })
  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': f'{MongoKey}',
    'Accept': 'application/ejson' 
  }

  #Ejecutamos un try para hacer el request a la API, esto nos devolverá un string
  try:
    response = requests.request("POST", url, headers=headers, data=payload) 

  #En caso de error de conexión cierra el interprete
  except requests.exceptions.ConnectionError:
    print('Error de conexion o falta de acceso a internet')
    quit()

  #En caso de Timout cierra el interprete
  except requests.exceptions.Timeout:
    print('Error de Timeout')
    quit()
    
  else:
    #Comprueba que response sea un string
    if type(response.text) == str:  
      result = (response.text)
    else:
      return 'El response no es un string'
  

    #Result es igual a la coleccion de bicicletas str
    return result


