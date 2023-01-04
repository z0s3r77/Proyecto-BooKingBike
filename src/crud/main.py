import src.db.crud as CRUD



def insertarArchivoJson(jsonFile):

    result = CRUD.insert_json(jsonFile)
    return result



def insertarDocumento(_id,brand,modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, modelWheelSize, modelWeight, priceday, status, location, img):
    
    result = CRUD.create(_id,brand,modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, modelWheelSize, modelWeight, priceday, status, location, img)
    return result
    


def actualizarDocumento(targetId, field, value):
    
    result = CRUD.update(targetId, field, value)
    return result



def buscarDocumento(id):

    result = CRUD.read(id)
    return result
    


def mostrarTodosLosDocumentos():

    result = CRUD.readall()
    return result
    


def borrarDocumento(id):

    result = CRUD.delete(id)
    return result




