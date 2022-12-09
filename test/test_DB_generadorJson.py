import pytest
from src.db.generadorJson import convertResponseStringIntoObjtect, generateJsonFileFromResponse

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

