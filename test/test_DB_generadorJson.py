import pytest
from src.db.generadorJson import convertResponseStringIntoObjtect, generateJsonFileFromResponse, checkSchemaDocument

prueba1 = """

[
    {
        "Nombre":"Sebas",
        "Apellido":"Estacio",
        "Edad":"21"
    },
    {
        "Nombre":"Miguel",
        "Apellido":"Vidal",
        "Edad":"21"
    }
]

"""
resultado_prueba1 = [{'Nombre': 'Sebas', 'Apellido': 'Estacio', 'Edad': '21'}, {'Nombre': 'Miguel', 'Apellido': 'Vidal', 'Edad': '21'}]
resultado_prueba2 = {'documents': [{'Nombre': 'Sebas', 'Apellido': 'Estacio', 'Edad': '21'}, {'Nombre': 'Miguel', 'Apellido': 'Vidal', 'Edad': '21'}]}
resultado_prueba3 = {'documents': [{'_id': 'B1', 'Brand': 'Nukeproof', 'Model': {'Name': 'MTB', 'Style': 'Rígida', 'Suspension': 'Suspension simple', 'Material': 'Aluminio', 'Fork brand': 'Marzocchi', 'Fork length': {'$numberInt': '140'}, 'Developments': '1x12', 'Group': 'Nukeproof Scout', 'Type': 'manual', 'Wheel size': {'$numberDouble': '29'}, 'Weight': {'$numberDouble': '13.5'}}, 'Price': {'$numberInt': '76'}, 'Status': 'avaliable', 'Location': 'Palma', 'img': 'https://images.internetstores.de/products/1921560/02/c6f242/nukeproof-scout-290-comp-asian-built-bullet-grey-1.jpg?forceSize=true&forceAspectRatio=true&useTrim=true&size=2400x2400'},
{'_id': 'B2', 'Brand': 'Orbea', 'Model': {'Name': 'MTB', 'Style': 'Cross Country', 'Suspension': 'Double suspension', 'Material': 'Carbono', 'Fork brand': 'Fox', 'Fork length': {'$numberInt': '140'}, 'Developments': '1x12', 'Group': 'Orbea Occram', 'Type': 'manual', 'Wheel size': {'$numberDouble': '29'}, 'Weight': {'$numberDouble': '13.65'}}, 'Price': {'$numberInt': '60'}, 'Status': 'available', 'Location': 'Santanyi', 'img': 'https://images.internetstores.de/products/1491758/02/bf7323/orbea-occam-m30-ice-green-jade-green-1.jpg?forceSize=true&forceAspectRatio=true&useTrim=true&size=2400x2400'}]}



def test_convertResponseStringIntoObject():

    #A la funcion se le pasa un str y comprueba si es formato JSON,
    #En caso de serlo, convierte el str en Objeto Python 

    assert convertResponseStringIntoObjtect(123123) == False
    assert convertResponseStringIntoObjtect("Esto es un string sin formato JSON") == False
    assert type(convertResponseStringIntoObjtect(prueba1)) == list
    assert convertResponseStringIntoObjtect(prueba1) == resultado_prueba1


def test_generateJsonFileFromResponse():
    #A la funcion se le pasas una lista de documentos y crea un directorio json 
    # y añade el contenido

    assert generateJsonFileFromResponse("Esto no es una lista con diccionarios", "prueba") == False
    assert generateJsonFileFromResponse(resultado_prueba2, "prueba") == True


def test_checkSchemaDocument():
    #A la funcion se le pasa un argumento, este argumento debe ser un diccionario con un array 
    #con los documentos de la colección Bicicleta
    
    assert checkSchemaDocument(213132) == False
    assert checkSchemaDocument("Esto no es un documento") == False
    assert checkSchemaDocument(resultado_prueba2) == False
    assert checkSchemaDocument(resultado_prueba3) == True