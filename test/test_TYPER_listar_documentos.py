from typer.testing import CliRunner
from src.typer.main import app
import pytest

runner = CliRunner()

@pytest.mark.test_TYPER_primera_parte
def test_listarDocumentos():
    
    result = runner.invoke(app, ["listar-documento"], input="B5")
    assert result.exit_code == 0
    assert "finalizado" in result.stdout

    result = runner.invoke(app,  ["listar-documento"], input="2342")
    assert result.exit_code == 0
    assert "No existe ningún documento con ID:  2342" in result.stdout

    result = runner.invoke(app, ["listar-documento", "--todos"])
    assert result.exit_code == 0
    assert "Finalizado con exito" in result.stdout

