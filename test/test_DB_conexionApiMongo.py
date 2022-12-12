import pytest
from src.db.conexionApiMongo import requestToMongoApi

@pytest.mark.test_DB
def test_requestToMongoApi():
    #Comrpobamos que la respuesta sea un str
    assert type(requestToMongoApi()) == str
