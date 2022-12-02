import requests
import json

# Creamos una función que nos permite hacer una petición de datos a MongoAtlas
# En esta petición(request) obtenemos como respuesta la colección de bikes

def requestToMongoApi():
  
  url = "https://data.mongodb-api.com/app/data-cozpc/endpoint/data/v1/action/find"
  payload = json.dumps({
      "collection": "bikes",
      "database": "BookingBike",
      "dataSource": "Sandbox",
      "filter": {"Brand":"shimano"},
      "projection":{
        "_id":1,
        "Brand":1,
        "Model":1,
        "Price":1,
        "Status":1
        }
  })
  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'yvkotEFnlbULNH9Zm14y8LSGZMYcbuA26YF5P9nZlXDpG4LEcEhlJYI3tALDVh5q',
    'Accept': 'application/ejson' 
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  result = (response.text)
  
  
  return result


