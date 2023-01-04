import pytest
from src.crud.main import * 

result = [
    {
        '_id': 'B4',
        'Brand': 'Orbea',
        'Model': {
            'Name': 'E-CityBike',
            'Style': 'E-Bike 25km/h',
            'Suspension': 'front suspension',
            'Material': 'Aluminio',
            'Fork brand': 'Ebikemotion',
            'Fork length': '160',
            'Developments': '1x12',
            'Group': 'Orbea Vibe',
            'Type': 'manual',
            'Wheel size': 28.0,
            'Weight': 21.2
        },
        'Price': 52,
        'Status': 'rented',
        'Hangar': 'H3',
        'Location': 'Campos',
        'img': 'https://images.internetstores.de/products/1368237/02/4d6f61/orbea-vibe-mid-h10-black-1.jpg?forceSize=true&forceAspectRatio=true&useTrim=true&size=2400x2400'
    }
]

@pytest.mark.test_crud
def test_read():
    #Pasamos un valor correcto a read
    assert buscarDocumento('B4') == result

    #Pasamos un valor int a read
    assert buscarDocumento(242432) == "[red]No hay ningún documento con ese ID[/red]"

    #Pasamos un string que no existe a read
    assert buscarDocumento('Esto no es un documento') == "[red]No hay ningún documento con ese ID[/red]"


@pytest.mark.test_crud
def test_readall():
    #La función readall nos devuelve una lista con todos los documentos
    assert type(mostrarTodosLosDocumentos()) == list


@pytest.mark.test_crud
def test_create():
    #Probamos 
    assert insertarDocumento(_id ="H103",brand="Apple", modelName="Electronica", modelStyle="Ciclocross", modelSuspension="no suspension",modelMaterial="Carbono",modelForkBrand="Apple",modelForklenght="160",modelDevelopments="1x13", modelGroup="Ortler", modelType="Bozen",modelWheelSize="28", modelWeight="9.1", priceday="70", status="avaliable", location="Manacor", img="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg\n") == "[blue]Se ha insertado el documento correctamente[/blue]"


@pytest.mark.test_crud
def test_update():
    #Probamos
    assert actualizarDocumento(targetId="H103", field="brand", value="Sony") == "[blue]Se ha actualizado el documento correctamente[/blue]"


@pytest.mark.test_crud
def test_insert_json():
    #Probamos
    assert insertarArchivoJson(jsonFile="test/pruebas/buenjson.txt") == "[blue]Se ha insertado el archivo correctamente el archivo JSON[/blue]"


@pytest.mark.test_crud
def test_delete():
    #Probamos
    assert borrarDocumento(id="H103") == '[blue]Se ha borrado el documento correctamente[/blue]'
    assert borrarDocumento(id="BSebas") == '[blue]Se ha borrado el documento correctamente[/blue]'
    assert borrarDocumento(id="GMiguel") == '[blue]Se ha borrado el documento correctamente[/blue]'