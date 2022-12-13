import pytest
from src.crud.main import mongoDBcrud

result = [
    {
        '_id': 'B5',
        'Brand': 'RONDO',
        'Model': {
            'Name': 'RoadBike',
            'Style': 'Gravel',
            'Suspension': 'none',
            'Material': 'Aluminio',
            'Fork brand': 'RONDO',
            'Fork length': '160',
            'Developments': '2x11',
            'Group': 'RONDO Ruut',
            'Type': 'manual',
            'Wheel size': 20.0,
            'Weight': 10.5
        },
        'Price': 31,
        'Status': 'available',
        'Hangar': 'H1',
        'Location': 'Palma',
        'img': 'https://images.internetstores.de/products/1736102/02/bba211/rondo-ruut-al-2-gravel-plus-black-black-1.jpg?forceSize=true&forceAspectRatio=true&useTrim=true&size=2400x2400'
    }
]

@pytest.mark.test_crud
def test_read():
    #Pasamos un valor correcto a read
    assert mongoDBcrud.read('B5') == result

    #Pasamos un valor int a read
    assert mongoDBcrud.read(242432) == False

    #Pasamos un string que no existe a read
    assert mongoDBcrud.read('Esto no es un documento') == False

@pytest.mark.test_crud
def test_readall():
    #La función readall nos devuelve una lista con todos los documentos
    assert type(mongoDBcrud.readall()) == list

@pytest.mark.test_crud
def test_create():
    #Probamos 
    assert mongoDBcrud.create(_id ="H103",brand="Apple", modelName="Electronica", modelStyle="Ciclocross", modelSuspension="no suspension",modelMaterial="Carbono",modelForkBrand="Apple",modelForklenght="160",modelDevelopments="1x13", modelGroup="Ortler", modelType="Bozen",modelWheelSize="28", modelWeight="9.1", priceday="70", status="avaliable", location="Manacor", img="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg\n") == True

@pytest.mark.test_crud
def test_update():
    #Probamos
    assert mongoDBcrud.update(targetId="H103", field="brand", value="Sony") == True


@pytest.mark.test_crud
def test_insert_json():
    #Probamos
    assert mongoDBcrud.insert_json(jsonFile="test/pruebas/buenjson.txt") == True


@pytest.mark.test_crud
def test_delete():
    #Probamos
    assert mongoDBcrud.delete(id="H103") == '[blue]Se ha borrado el documento correctamente[/blue]'
    assert mongoDBcrud.delete(id="BSebas") == '[blue]Se ha borrado el documento correctamente[/blue]'
    assert mongoDBcrud.delete(id="GMiguel") == '[blue]Se ha borrado el documento correctamente[/blue]'