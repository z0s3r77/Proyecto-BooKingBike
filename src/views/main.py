from src.db.convertirJsonALista import bikes_json
from datetime import datetime
import sys

# Comprobar que existe bikes_json
assert isinstance(bikes_json, list)


# HEAD

def html_head(title='Booking Bike', description='Booking Bike'):
    # Obtenemos la fecha actual
    date = datetime.today().strftime('%Y-%m-%d')
    head = f"""<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="author" content="Miguel & Sebastian">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name='description' content='Pagina de inicio de BookingBike'>
        <meta name="keywords" content="MTB, Ebike , CityBike, Bikes , Renting">
        <meta http-equiv="last-modified" content='2022-12-01'>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/3714/3714324.png">
        <title>Contacto</title>
    </head>"""
    print(head)


# BODY

class body():

    # Body para home

    def body_pagina_principal():
        body = """    <body>
        <header>
            <h1>BookingBike</h1>
        </header>
        <nav>
            <ul>
                <li><a href="listadototalbicis.html">Todas las bicis</a></li>
                <li><a href="listadomarcabicis.html"> Marcas disponibles</a></li>
                <li><a href="listadotipobicis.html"> Modelos disponibles</a></li>            
                <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>            
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
        </nav>
        <main>
            <div>
                <h4>¿Quienes somos?</h4>
                <p>Somos una empresa fundada en España en el año 2022 con el objetivo de ayudar a la ciudadania
                    y al medio ambiente a ir hacia un futuro mejor y ecosostenible. 
                </p>
            </div>
            <div>
                <h4>¿Que hacemos?</h4>
                <p>Hemos creado una plataforma donde los ciudadanos pueden comprobar la disponibilidad de bicicletas 
                    en alquiler en un área determinada. Para esto, todas las empresas <u>certificadas</u> de alquiler
                    de bicicletas que estén interesadas pueden volcar su catálago con nosotros.
                </p>
            </div>
            <div>
                <h4>¿Como reservar?</h4>
                <p> <b>!Sencillo!</b> Tan solo debes dirigirte a uno de los enlaces que tienes disponibles en nuestra barra de navegación.
                    Puedes ver todo el <i>"arsenal"</i> de bicicletas al completo o filtrar por modelo o marca. Una vez, seleccionada
                    la que más te conviene, tan solo haz <u>clic</u> en <b>Reservar</b> y te indicaremos los siguientes pasos.  
                </p>
            </div>
            <div>
                <h4>¿Por que BookingBike?</h4>
                <p>Porque ahora, alquilar tu bicicleta favorita para cada época del año es más sencillo de lo que te imaginas.
                    Nosotros te mostramos todo el cátalogo disponible en tu zona, tú eres el encargado o encargada de seleccionar
                    la que mejor se adapte a tí y en tan solo unos días la tendrás en la puerta de tu casa. <b>Así de simple!</b>
                </p>
            </div>
        </main>"""
        print(body)

    # Body para la pagina de contacto

    def body_contacto():
        body = """    <body>
        <header>
            <h1>Pagina de contacto</h1>
        </header>
        <main>
            <section>
                <form>
                    <fieldset>
                        <legend>Contacta con nosotros</legend>
                        <label for='nombre'> Nombre: </label>
                        <input type='text' name='nombre' id='nombre'><br><br>
                        <label for='correo'> Correo: </label>
                        <input type='text' name='correo' id='correo'><br><br>
                        <label for='mensaje'> Mensaje: </label><br>
                        <textarea type='text' name='mensaje' id='mensaje'></textarea><br>
                        <input type='submit' value='enviar'>
                        <input type='reset' value='borrar'>
                    </fieldset>
                </form>
            </section>
        </main>"""
        print(body)

    def body_listado_total_bicis():
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>
        <nav>
            <ul>
                <li><a href="home.html">Inicio</a></li>
                <li><a href="listadomarcabicis.html"> Marcas disponibles</a></li>
                <li><a href="listadotipobicis.html"> Modelos disponibles</a></li>            
                <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>            
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
        </nav>
        <section>
            <div>""")
        x = 0
        while x <= (len(bikes_json)-1):
                print("""                <div>
                    <img alt="imagen"></img>
                    <br>"""
                    f"<a href='{bikes_json[x]['_id']}.html'> <b>""", bikes_json[x]['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", bikes_json[x]['Model']['Name']  ,"""27,5<br>
                    """,bikes_json[x]['Price']['$numberInt']+"€/dia <br>"
                """</div><br>""")
                x += 1

        print("""                </div>
        </section>""")
    
    # Body para la los tipos de bicis

    def body_listado_tipo_bicis():
        print("""<body>
    <header>
        <h1>Listado de tipos de Bicis </h1>
    </header>
    <nav>
        <ul>
            <li><a href="home.html">Inicio</a></li>
            <li><a href="listadototalbicis.html">Todas las bicis</a></li>
            <li><a href="listadomarcabicis.html"> Marcas disponibles</a></li>
            <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>            
            <li><a href="contacto.html">Contacto</a></li>
        </ul>
    </nav>
    <section>
        <div>""")

        x = 0
        tipos_bicis = []
        while x <= (len(bikes_json)-1):

            tipo = bikes_json[x]['Model']['Name']

            if tipo in tipos_bicis:
                pass
            else:
                tipos_bicis.append(tipo)

            x += 1
        
        for x in tipos_bicis:
            enlace = "<a href='{}.html'> {} </a>".format(x,x)
            print("            <div>",enlace ,"</div>")  
        print("""        </div>
    </section>""")
        
    # Body para las marcas de bicis 

    def body_listado_marca_bicis():
        print("""<body>
    <header>
        <h1>Listado de bicis por marca </h1>
    </header>
    <nav>
        <ul>
            <li><a href="home.html">Inicio</a></li>
            <li><a href="listadototalbicis.html">Todas las bicis</a></li>
            <li><a href="listadotipobicis.html"> Tipos disponibles</a></li>
            <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>            
            <li><a href="contacto.html">Contacto</a></li>
        </ul>
    </nav>
    <section>
        <div>""")

        x = 0
        tipos_bicis = []
        while x <= (len(bikes_json)-1):

            tipo = bikes_json[x]['Brand']

            if tipo in tipos_bicis:
                pass
            else:
                tipos_bicis.append(tipo)

            x += 1
        
        for x in tipos_bicis:
            enlace = "<a href='{}.html'> {} </a>".format(x,x)
            print("            <div>",enlace ,"</div>")  
        print("""        </div>
    </section>""")

    #Ojo da error porque todavia no tenemos el campo de Location

    def body_listado_por_zona_bicis():
        print("""<body>
    <header>
        <h1>Listado de Bicis por zona </h1>
    </header>
    <nav>
        <ul>
            <li><a href="home.html">Inicio</a></li>
            <li><a href="listadototalbicis.html">Todas las bicis</a></li>
            <li><a href="listadotipobicis.html"> Tipos disponibles</a></li>
            <li><a href="listadomarcabicis.html"> Marcas disponibles </a></li>            
            <li><a href="contacto.html">Contacto</a></li>
        </ul>
    </nav>
    <section>
        <div>""")

        x = 0
        tipos_bicis = []
        while x <= (len(bikes_json)-1):

            tipo = bikes_json[x]['Location']

            if tipo in tipos_bicis:
                pass
            else:
                tipos_bicis.append(tipo)

            x += 1
        
        for x in tipos_bicis:
            enlace = "<a href='{}.html'> {} </a>".format(x,x)
            print("            <div>",enlace ,"</div>")  
        print("""        </div>
    </section>""")

# FOOTER


def footer():
    footer = """        <footer>
            <p>Esta página es de @Miguel & @Sebastian</p>
            <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licencia Creative Commons"
                    style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Esta obra
            está
            bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Licencia Creative Commons
                Atribución-NoComercial 4.0 Internacional</a>.
        </footer>
    </body>
</html>"""
    print(footer)


# GENERANDO PAGINAS


def pagina_principal():
    sys.stdout = open('home.html', 'w', encoding="UTF-8")
    html_head(title="Pagina principal - BookingBike",
              description='Pagina de inicio de BookingBike')
    body.body_pagina_principal()
    footer()
    sys.stdout.close()


def contacto():
    sys.stdout = open('contacto.html', 'w', encoding="UTF-8")
    html_head(title="Pagina de contacto - BookingBike",
              description='Pagina de para contactar con la organización')
    body.body_contacto()
    footer()
    sys.stdout.close()


def listado_total_bicis():
    sys.stdout = open('listadototalbicis.html', 'w', encoding="UTF-8")
    html_head(title="Listado de bicis - BookingBike",
              description='Pagina que muestra todas las bicis disponibles')
    body.body_listado_total_bicis()
    footer()
    sys.stdout.close()

def listado_tipo_bicis():
    sys.stdout = open('listadotipobicis.html', 'w', encoding="UTF-8")
    html_head(title="Tipos de bicis disponibles - BookingBike",
              description='Pagina que muestra todos los tipos de bicis disponibles')
    body.body_listado_tipo_bicis()
    footer()
    sys.stdout.close()

def listado_marca_bicis():
    sys.stdout = open('listadomarcabicis.html', 'w', encoding="UTF-8")
    html_head(title="Marcas de bicis disponibles - BookingBike",
              description='Pagina que muestra todas las marcas de bicis disponibles')
    body.body_listado_marca_bicis()
    footer()
    sys.stdout.close()

def listado_zona_bicis():
    sys.stdout = open('listadobicisporzona.html', 'w', encoding="UTF-8")
    html_head(title="Bicis disponible por zona - BookingBike",
              description='Pagina que muestra todas las zonas que tienen bicis disponibles')
    body.body_listado_por_zona_bicis()
    footer()
    sys.stdout.close()


pagina_principal()
contacto()
listado_total_bicis()
listado_tipo_bicis()
listado_marca_bicis()
listado_zona_bicis()