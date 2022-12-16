import json
import time
from src.db.MongoAtlasConexion import MongoAtlas


# Se crea una clase con diferentes metodos
#Dichos metodos se usan en src/typer/main.py

class mongoDBcrud():

    #Este metodo suber un archivo JSON a la colección Bikes
    def insert_json(jsonFile):

        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        
        #Comprobamos que el archivo sea un JSON
        with open(jsonFile) as jFile:
            file_content = jFile.read()
        try:
            json.loads(file_content)
        except ValueError:
            print("La ruta es correcta pero el archivo no es de tipo JSON")
            quit()
        else:
            print("El archivo es JSON")
        

        #Al ser JSON , se itera sobre el y se suben los documentos 
        with open(jsonFile) as file:
            file_data = json.load(file)
            
        if isinstance(file_data, list):
            BikesCollection.insert_many(file_data)
        else:
            BikesCollection.insert_one(file_data)


        #Por cada documento, se nos muestra si se ha insertado
        for i in file_data:
            
            i['_id']

            check = BikesCollection.find_one({'_id':i['_id']})

            if check:
                pass
            elif check == None:
                return (f"No se ha podido insetar el documento con id {i['_id']}")

            return True
        




    #Este metodo pide los datos para completar el documento JSON
    #Seguidamente sube el resultado

    def create(_id,brand,modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, modelWheelSize, modelWeight, priceday, status, location, img):
        
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
            
        query = {
                "_id" : _id,
                "Brand": brand,
                "Model" : {
                    "Name": modelName,
                    "Style": modelStyle,
                    "Suspension": modelSuspension,
                    "Material": modelMaterial,
                    "Fork brand": modelForkBrand,
                    "Fork length": {"$numberInt": modelForklenght},
                    "Developments": modelDevelopments,
                    "Group": modelGroup,
                    "Type": modelType,
                    "Wheel size":{  "$numberDouble": modelWheelSize},
                    "Weight": {  "$numberDouble": modelWeight}
                },
                "Price": { "$numberInt": priceday},
                "Status": status,
                "Hangar": "H6",
                "Location": location,
                "img": img
            }

        try:
            BikesCollection.insert_one(query)
            return True
        except:
            return False


    #Este metodo toma un ID de documento, un campo y un valor nuevo y lo actualiza
    def update(targetId, field, value ):
        
        values = {field:value}

        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"] 

        query = {"_id": targetId}
        newValues = {"$set": values}



        if BikesCollection.update_one(query, newValues) == False:
            return False
        else:
            return True


    #Este metodo tan solo muestra el documento por su ID
    def read(id):

        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        #Se guarda el documento en un array para poder hacerle un print (rich) desde src/typer/main.py
        result = []
        if BikesCollection.count_documents (query, limit=1) != 0:
            print('')
            for x in BikesCollection.find(query):
                result.append(x)
        
            return result
        else:
            return False


    #Este metodo toma todos los documentos de la base de datos y los envia a src/typer/main.py
    def readall():

        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        
        time.sleep(3)
        
        result=[]

        for x in BikesCollection.find():
            result.append(x)

        if len(result) == 0:
            return False
        else:
            return result


    #Este metodo borra el documento según su ID
    def delete(id):

        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        if mongoDBcrud.read(id) == False:
            result = '[red]No hay ningún documento con ese ID[/red]'
            return result

        try:
            BikesCollection.delete_one(query)
        except:
            result = '[red]Algo ha ido mal, no se ha podido borrar[/red]'
            return result
        else:
            result = '[blue]Se ha borrado el documento correctamente[/blue]'
            return result
