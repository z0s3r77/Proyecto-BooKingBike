import pytest
from src.db.MongoAtlasConexion import connect


def test_MongoAtlasConexion():
    #Comprobamos que no se pueda introducir un host invalidado
    assert connect(host='OIhsioahd') == False
    assert connect(host='https://www.mongodb.com/atlas/app-services/data-api') == True


