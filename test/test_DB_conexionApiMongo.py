import pytest
from src.db.conexionApiMongo import requestToMongoApi

@pytest.mark.test_response
def test_requestToMongoApi():
    #Comrpobamos que la respuesta sea un str
    assert type(requestToMongoApi()) == str
