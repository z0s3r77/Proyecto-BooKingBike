from typer.testing import CliRunner
from src.typer.main import app
import pytest

runner = CliRunner()

@pytest.mark.test_TYPER_segunda_parte
def test_actualizarDocumentos():
    
    #Insertar un ID que no existe para actualizar
    result = runner.invoke(app, ["actualizar-documento"], input="4234")
    assert result.exit_code == 0
    assert "No hay ningún documento con ese ID" in result.stdout

    #Actualizar correctamente un documento
    result = runner.invoke(app, ["actualizar-documento"], input="BSebas\n Nombre\n Federico\n")
    assert result.exit_code == 0
    assert "Proceso finalizado" in result.stdout