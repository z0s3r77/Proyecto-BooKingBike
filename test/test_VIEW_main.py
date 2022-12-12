import pytest
import os 



@pytest.mark.lanzar_main
def test_lanzar_main():
    import src.views.main 
    assert os.path.exists("json/") == True
    assert os.path.exists("docs/") == True





@pytest.mark.comprobar_rutas_html
def test_main():
    #Se comprueba que se creen todos los archivos después de ejecutar el archivo VIEWS_main.py
    assert os.path.exists("docs/bikes") == True
    assert os.path.exists("docs/brand") == True
    assert os.path.exists("docs/css") == True
    assert os.path.exists("docs/developments") == True
    assert os.path.exists("docs/location") == True
    assert os.path.exists("docs/shifts") == True
    assert os.path.exists("docs/wheelsize") == True
    assert os.path.exists("docs/index.html") == True