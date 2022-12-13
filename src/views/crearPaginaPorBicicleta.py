from src.db.convertirJsonALista import convertJsonToList
from src.views.funcionesHTML import *
import sys

#Llamamos a la función que convierte en lista el archivo json


bikes_json = convertJsonToList('json/bikes.json')

#Genera una pagina por cada bici de la base de datos

def pagina_por_bicicleta():

    x = 0
    while x <= (len(bikes_json)-1):

        page = 'docs/bikes/' +bikes_json[x]['_id'] + '.html'
        sys.stdout = open(f'{page}', 'w', encoding="UTF-8")
        html_head_externo(title="BookingBike",
                  description='Bici en concreto')
        print("""    <body>
        <header>
            <h1 class="header">BooKingBike</h1>
        </header>""")
        nav_body_externo()
        print("""        <main class="specifications-group">
            <!--Añadimos toda la información de la bici-->
            <h2>Especificaciones técnicas:</h2>
            <div >""")
        print(f"""                <img class="responsive-sale" alt="B2" width="500" height="450"  src="{bikes_json[x]['img']}">
                <div class=specifications-move">
                    <p class="specifications">
                        <b>Marca:</b>""",bikes_json[x]['Brand'],""" <br>
                        <b>Bicicleta de tipo: </b>""",bikes_json[x]['Model']['Name'],""" <br>
                        <b>Estilo:</b> """,bikes_json[x]['Model']['Style'],"""  <br>
                        <b>Tipo de cambios:</b> """,bikes_json[x]['Model']['Type'],"""  <br>
                        <b>Material:</b> """,bikes_json[x]['Model']['Material'],"""  <br>
                        <b>Tamaño de las ruedas: </b> 20" <br>
                        <b>Desarrollos:</b> """,bikes_json[x]['Model']['Developments'],"""  <br>
                        <b>Localizacion:</b> Palma <br>
                        <b>Precio por día:</b> """,bikes_json[x]['Price']['$numberInt']+"""€ <br>
                    </p>
                    <button class="sale"><a href="#aningunlugar">RESERVAR</a></button>
                </div>
            </div>
        </main>""")
        footer()

        sys.stdout.close()

        x += 1
