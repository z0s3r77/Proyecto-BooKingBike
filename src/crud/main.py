import pymongo
import json
import time


class mongoDBcrud():

    def insert_json(jsonFile):

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        with open(jsonFile) as file:
            file_data = json.load(file)
            
        if isinstance(file_data, list):
            BikesCollection.insert_many(file_data)
        else:
            BikesCollection.insert_one(file_data)


        for i in file_data:
            
            i['_id']

            check = BikesCollection.find_one({'_id':i['_id']})

            if check:
                print(f"Se ha insertado correctamente el nuevo documento con id {i['_id']}")
            elif check == None:
                print(f"No se ha podido insetar el documento con id {i['_id']}")

        





    def create(_id, brand, modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, priceday, status):
        
        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
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
            "Fork length": modelForklenght,
            "Developments": modelDevelopments,
            "Group": modelGroup,
            "Type": modelType
            },
            "Price": priceday,
            "Status": status
        }


        insert = BikesCollection.insert_one(query)


        # if check == True:
        #     print("Se ha insertado correctamente el nuevo documento")
        # else:
        #     print("No se ha podido insetar el documento")

      






    def update(targetId, field, value ):
        
        values = {field:value}

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"] 

        query = {"_id": targetId}
        newValues = {"$set": values}


        BikesCollection.update_one(query, newValues)



    def read(id):

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        result = []

        if BikesCollection.count_documents (query, limit=1) != 0:
            print('')
            for x in BikesCollection.find(query):
                result.append(x)
        
            return result
        else:
            result = f'[red]No existe ningún documento con ID:[/red]  {id}'
            return result



    def readall():

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        
        time.sleep(3)
        
        result=[]

        for x in BikesCollection.find():
            result.append(x)

        return result


    def delete(id):
        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        BikesCollection.delete_one(query)


