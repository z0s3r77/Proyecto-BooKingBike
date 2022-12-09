import pytest
from src.db.convertirJsonALista import checkBikesJsonFile, convertBikesJsonToList

resultado = [
    {
        "Nombre": "Sebas",
        "Apellido": "Estacio",
        "Edad": "21"
    },
    {
        "Nombre": "Miguel",
        "Apellido": "Vidal",
        "Edad": "21"
    }
]

def test_checkBikesJsonFile():

    #A la función se le pasa la ruta de un fichero 
    #y comprueba si tiene formato JSON 

    assert checkBikesJsonFile(23323) == False
    assert checkBikesJsonFile('Esto no es un fichero') == False
    assert checkBikesJsonFile('test/pruebas/maljson.txt') == False 
    assert checkBikesJsonFile('test/pruebas/buenjson.txt') == True


def test_convertBikesJsonToList():

    #A la función se le pasa la ruta de un fichero 
    #En caso de tener formato JSON devuelve el valor en una lista

    assert convertBikesJsonToList(22233) == False
    assert convertBikesJsonToList('Esto no es un parametro valido') == False
    assert convertBikesJsonToList('test/pruebas/maljson.txt') == False
    assert type(convertBikesJsonToList('test/pruebas/buenjson.txt')) == list
    assert convertBikesJsonToList('test/pruebas/buenjson.txt') == resultado