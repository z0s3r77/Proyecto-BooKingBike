from typer.testing import CliRunner
from src.typer.main import app
import pytest

runner = CliRunner()

@pytest.mark.test_TYPER_segunda_parte
def test_borrarDocumentos():

    #Probamos introduciendo un ID que no existe    
    result = runner.invoke(app, ["borrar-documento"], input="BICICLETAS")
    assert result.exit_code == 0
    assert "No hay ningún documento con ese ID" in result.stdout

    #Probamos insertando un ID que si existe
    result = runner.invoke(app, ["borrar-documento"], input="H100")
    assert result.exit_code == 0
    assert "Se ha borrado el documento correctamente" in result.stdout

    #Probamos insertando un ID que si existe
    result = runner.invoke(app, ["borrar-documento"], input="BSebas")
    assert result.exit_code == 0
    assert "Se ha borrado el documento correctamente" in result.stdout

    #Probamos a borrar los dos ID que introducimos en otro test
    result = runner.invoke(app, ["borrar-documento"], input="GMiguel")
    assert result.exit_code == 0
    assert "Se ha borrado el documento correctamente" in result.stdout
