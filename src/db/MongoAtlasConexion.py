import pymongo
import urllib.request
from dotenv import dotenv_values
import os

#Check conexion MongoAtlas
def connect(host):

  if host != 'https://www.mongodb.com/atlas/app-services/data-api':
    print('No ha introducido la URL correcta')
    return False
  else:
    pass

  try:
    urllib.request.urlopen(host)
    return True
  except:
    print("No es posible acceder a Mongo Atlas")
    return False

if connect(host='https://www.mongodb.com/atlas/app-services/data-api') == False:
  quit()



config = dotenv_values(".env")


#Modulo que guarda variables importantes

MongoAtlas = pymongo.MongoClient(config["ATLAS_URI"])
MongoKey = config["Key"]

