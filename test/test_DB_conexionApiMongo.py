import pytest
from src.db.conexionApiMongo import requestToMongoApi

def test_requestToMongoApi():
    #Comrpobamos que la respuesta sea un str
    assert type(requestToMongoApi()) == str
