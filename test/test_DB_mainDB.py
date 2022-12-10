import pytest
from src.db.mainDb import generateJsonFromResponseApi, getListfromJsonFile, mainDB
import os

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

@pytest.mark.test_generarUnFicheroJsonDeLaRespuestaAPI
def test_generateJsonFromResponseApi():
    
    #La función nos genera un json con el nombre del parametro
    #Cuyo contenido es la respuesta de la API
    #EL modulo generadorJSON se encarga de comproboar si existe o no
    #Por ese motivo, no se vuelve a testear que se haya creado el fichero

    assert generateJsonFromResponseApi('prueba') == True
    assert generateJsonFromResponseApi(1232) == False
    assert generateJsonFromResponseApi('prueba2') == True


@pytest.mark.test_generarListaDesdeUnFicheroJSON
def test_getListfromJsonFile():

    #La funcion genera un objeto List de un archivo JSON

    assert type(getListfromJsonFile('test/pruebas/buenjson.txt')) == list
    assert getListfromJsonFile('test/pruebas/buenjson.txt') == resultado
    assert getListfromJsonFile(23123) == False
    assert getListfromJsonFile('Esto no es un fichero') == False
    assert getListfromJsonFile(['Esto','Tampoco',2313]) == False
    assert getListfromJsonFile({"Esto":"Es un dict"}) == False


@pytest.mark.test_generarElArchivoBikesYQueSeDevuelvaUnaLista
def test_mainDB():

    #MainDB obtiene una ruta y el nombre del fichero.
    #Primero carga el response de la API en el fichero dentro de la ruta
    #Luego selecciona ese mismo fichero y devuelve una lista con los documentos

    assert type(mainDB('json/bikes.json','bikes')) == list
    assert mainDB('rutamala/bikes.json', 'bikes') == False