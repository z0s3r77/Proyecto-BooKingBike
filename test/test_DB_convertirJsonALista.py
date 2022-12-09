import pytest
from src.db.convertirJsonALista import checkBikesJsonFile, convertBikesJsonToList


def test_checkBikesJsonFile():

    #A la función se le pasa la ruta de un fichero 
    #y comprueba si tiene formato JSON 

    assert checkBikesJsonFile(23323) == False
    assert checkBikesJsonFile('Esto no es un fichero') == False
    assert checkBikesJsonFile('test/pruebas/maljson.txt') == False 
    assert checkBikesJsonFile('test/pruebas/buenjson.txt') == True
