import pymongo



class mongoDBcrud():



    def create(_id, brand, modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, priceday, status):
        MongoAtlas = pymongo.MongoClient("mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/?retryWrites=true&w=majority")
        BookingBikeDb = MongoAtlas["BookingBike"]
        BikesCollection = BookingBikeDb["bikes"]
        
        # _id = input('Introduce un id: ')
        # brand = input('Introduce una brand: ')
        # modelName = input('Introduce el tipo de Bicicleta: ')
        # modelStyle = input('Introduce el estilo de Bicicleta: ')
        # modelSuspension = input('Introduce el tipo de suspencion: ')
        # modelMaterial = input('Introduce el material de la bicicleta: ')
        # modelForkBrand = input('Introduce la marca del Fork: ')
        # modelForklenght = input('Introduce la longitud del Fork: ')
        # modelDevelopments = input('Introduce el tipo de desarrollos: ')
        # modelGroup = input('Introduce grupo: ')
        # modelType = input('Introduce de que tipo es la bicicleta(manual o automatica): ')
        # priceday = input('Introduce el precio por día: ')
        # status = input('Introduce disponibildiad: (avaliable o rented)')

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



