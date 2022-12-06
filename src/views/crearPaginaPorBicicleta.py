from src.db.convertirJsonALista import bikes_json
from src.views.funcionesHTML import *
import sys


def pagina_por_bicicleta():

    x = 0
    while x <= (len(bikes_json)-1):

        page = 'docs/bikes/' +bikes_json[x]['_id'] + '.html'
        sys.stdout = open(f'{page}', 'w', encoding="UTF-8")
        html_head(title="BookingBike",
                  description='Bici en concreto')
        print("""<body>
    <header>
        <h1>BookingBike</h1>
    </header>
    <nav>
        <ul>
            <li><a href="../home.html">Inicio</a></li>
            <li><a href="../listadototalbicis.html">Todas las bicis</a></li>
            <li><a href="../listadomarcabicis.html"> Marcas disponibles</a></li>
            <li><a href="../listadotipobicis.html"> Modelos disponibles</a></li>            
            <li><a href="../listadobicisporzona.html"> Zonas disponibles </a></li>            
            <li><a href="../contacto">Contacto</a></li>
        </ul>
    </nav>
    <main>
        <h2>Especificaciones técnicas:</h2>
        <div>""")
        print(f"""<img alt="B2" width="500" height="450"  src="{bikes_json[x]['img']}">
            <div>
                <p>
                    <b>Marca:</b>""",bikes_json[x]['Brand'],""" <br>
                    <b>Bicicleta de tipo: </b>""",bikes_json[x]['Model']['Name'],""" <br>
                    <b>Estilo:</b> """,bikes_json[x]['Model']['Style'],"""  <br>
                    <b>Tipo de cambios:</b> """,bikes_json[x]['Model']['Type'],"""  <br>
                    <b>Material:</b> """,bikes_json[x]['Model']['Material'],"""  <br>
                    <b>Tamaño de las ruedas: </b> 20" <br>
                    <b>Desarrollos:</b> """,bikes_json[x]['Model']['Developments'],"""  <br>
                    <b>Localizacion:</b> Palma <br>
                    <b>Precio por día:</b> """,bikes_json[x]['Price']['$numberInt'],""" <br>
                </p>
                <a href="#aningunlugar">RESERVAR</a>
            </div>
        </div>
    </main>""")
        footer()

        sys.stdout.close()

        x += 1
