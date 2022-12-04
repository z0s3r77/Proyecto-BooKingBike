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
        <meta name='description' content='{description}'>
        <meta name="keywords" content="MTB, Ebike , CityBike">
        <meta http-equiv="last-modified" content='{date}'>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/3714/3714324.png">
        <title>{title}</title>
    </head>"""
    print(head)


# BODY

def body_pagina_principal():
    body = """<body>
    <header>
        <h1>BookingBike</h1>
    </header>
    <nav>
        <ul>
            <li><a href="listadototalbicis.html">Todas las bicis</a></li>
            <li><a href="listadomarcabicis.html"> Marcas disponibles</a></li>
            <li><a href="listadotipobicis.html"> Modelos disponibles</a></li>            
            <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>            
            <li><a href="#contacto">Contacto</a></li>
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


# FOOTER

def footer():
    footer = """<footer>
        <div>
            <p><i>Pagina realizada por @MiguelVidalt & @SebastianEstacio</i></p>
        </div>
    </footer>
    </body>
    </html>"""
    print(footer)

#GENERANDO HOME    

def pagina_principal():
    sys.stdout = open('home.html', 'w', encoding="UTF-8")
    html_head(title="Pagina principal - BookingBike", description='Pagina de inicio de BookingBike')
    body_pagina_principal()
    footer()
    sys.stdout.close()

pagina_principal()