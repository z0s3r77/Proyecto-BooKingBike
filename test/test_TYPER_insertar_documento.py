from typer.testing import CliRunner
from src.typer.main import app
import pytest

runner = CliRunner()

@pytest.mark.test_TYPER_primera_parte
def test_insertar_documento():

    # Probamos a insertar un documento correcto
    result = runner.invoke(app,  ["insertar-documento"], input="H100\n Apple\n Electronica\n Ciclocross\n no suspension\n Carbono\n Apple\n 160\n 1x13\n Ortler Bozen\n manual\n 28\n 9.1\n 70\n avaliable\n Manacor\n https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg\n y\n")
    assert result.exit_code == 0
    assert "Se ha insertado con exito" in result.stdout

    #Probamos a insertar un documento repetido
    result = runner.invoke(app,  ["insertar-documento"], input="H100\n Apple\n Electronica\n Ciclocross\n no suspension\n Carbono\n Apple\n 160\n 1x13\n Ortler Bozen\n manual\n 28\n 9.1\n 70\n avaliable\n Manacor\n https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg\n y\n")
    assert result.exit_code == 0
    assert "No se ha podido insertar el documento" in result.stdout

    #Pobramos a abortar el proceso
    result = runner.invoke(app,  ["insertar-documento"], input="H100\n Apple\n Electronica\n Ciclocross\n no suspension\n Carbono\n Apple\n 160\n 1x13\n Ortler Bozen\n manual\n 28\n 9.1\n 70\n avaliable\n Manacor\n https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg\n n\n")
    assert result.exit_code == 0
    assert "Se ha abortado el proceso" in result.stdout

    # Probamos a insertar una ruta incorrecta de un documento JSON como opción 
    result = runner.invoke(app,["insertar-documento", "--jsonfile", "estaruta/esincorrecta.json"] )
    assert result.exit_code == 0
    assert "No existe el archivo en la ruta especificada: estaruta/esincorrecta.json " in result.stdout

    # Probamos a pasarle un archivo TXT con una estructura erronea de JSON
    result = runner.invoke(app,["insertar-documento", "--jsonfile", "test/pruebas/maljson.txt"] )
    assert result.exit_code == 0
    assert "La ruta es correcta pero el archivo no es de tipo JSON" in result.stdout

    #Probamos a pasarle un documento JSON con formato correcto
    result = runner.invoke(app, ["insertar-documento", "--jsonfile", "test/pruebas/buenjson.txt"])
    assert result.exit_code == 0
    assert "Se han insertado todos los documentos" in result.stdout