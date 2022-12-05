import pymongo
import json


class mongoDBcrud():

    def insert_json(jsonFile):

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        with open(jsonFile) as file:
            file_data = json.load(file)

            print(file_data)

        # if isinstance(file_data, list):
        #     BikesCollection.insert_many(file_data)
        # else:
        #     BikesCollection.insert_one(file_data)



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






    def update(targetId, newvalues ):
        

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"] 

        query = {"_id": targetId}
        newValues = {"$set": newvalues}

        BikesCollection.update_one(query, newValues)

        for x in BikesCollection.find(query):
            print(x)



    def read(id):

        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        for x in BikesCollection.find(query):
            print(x, '\n')


    def delete(id):
        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]

        query = {"_id":id}

        BikesCollection.delete_one(query)



