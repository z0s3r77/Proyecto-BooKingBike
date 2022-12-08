# from src.db.convertirJsonALista import bikes_json
from src.db.convertirJsonALista import convertJsonToList
from src.views.creardiccionarios import *
from datetime import datetime
import sys
import os


bikes_json = convertJsonToList('json/bikes.json')

#Comprobar que existe bikes_json
assert isinstance(bikes_json, list)

"""
    COMPROBAMOS SI EXISTEN LAS CARPETAS, SI NO, LAS CREAMOS
"""

#Comprobamos si existe el directorio bikes , sino, lo crea
if not os.path.exists('docs/bikes/'):
    os.makedirs('docs/bikes/')

#Comprobamos si existe el directorio brand , sino, lo crea
if not os.path.exists('docs/brand/'):
    os.makedirs('docs/brand/')

#Comprobamos si existe el directorio location , sino, lo crea
if not os.path.exists('docs/location/'):
    os.makedirs('docs/location/')

#Comprobamos si existe el directorio types , sino, lo crea
if not os.path.exists('docs/types/'):
    os.makedirs('docs/types/')

#Comprobamos si existe el directorio wheelsize , sino, lo crea
if not os.path.exists('docs/wheelsize/'):
    os.makedirs('docs/wheelsize/')

#Comprobamos si existe el directorio developments , sino, lo crea
if not os.path.exists('docs/developments/'):
    os.makedirs('docs/developments/')

#Comprobamos si existe el directorio shifts , sino, lo crea
if not os.path.exists('docs/shifts/'):
    os.makedirs('docs/shifts/')

"""
    FUNCIONES QUE GENERAN LAS PARTES HTML
"""

# Comprobar que existe bikes_json
assert isinstance(bikes_json, list)


# HEAD

def html_head(title, description):
    # Obtenemos la fecha actual
    date = datetime.today().strftime('%Y-%m-%d')
    print(f"""<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="author" content="Miguel & Sebastian">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name='description' content='{description}'>
        <meta name="keywords" content="MTB, Ebike , CityBike, Bikes , Renting">
        <meta http-equiv="last-modified" content='2022-12-01'>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/3714/3714324.png">
        <title>"""+title+"""</title>
        </head>""")

# NAV
nav=("""        <nav>
            <ul>
                <li><a href="home.html">Inicio</a></li>
                <li><a href="listadototalbicis.html">Todas las bicis</a></li>
                <li><a href="listadomarcabicis.html"> Marcas disponibles</a></li>
                <li><a href="listadotipobicis.html"> Modelos disponibles</a></li>            
                <li><a href="listadobicisporzona.html"> Zonas disponibles </a></li>
                <li><a href="listadobicisportamañorueda.html">Tamaños de rueda disponibles </a></li>
                <li><a href="listadobicispordesarrollo.html">Desarollos disponibles </a></li>            
                <li><a href="contacto.html">Contacto</a></li>
            </ul>
        </nav>""")

nav_2=("""        <nav>
            <ul>
                <li><a href="../home.html">Inicio</a></li>
                <li><a href="../listadototalbicis.html">Todas las bicis</a></li>
                <li><a href="../listadomarcabicis.html"> Marcas disponibles</a></li>
                <li><a href="../listadotipobicis.html"> Modelos disponibles</a></li>            
                <li><a href="../listadobicisporzona.html"> Zonas disponibles </a></li>
                <li><a href="../listadobicisportamañorueda.html">Tamaños de rueda disponibles </a></li>
                <li><a href="../listadobicispordesarrollo.html">Desarollos disponibles </a></li>            
                <li><a href="../contacto.html">Contacto</a></li>
            </ul>
        </nav>""")

# BODY

class body():

    # Body para home

    def body_pagina_principal(nav):
        print("""    <body>
        <header>
            <h1>BookingBike</h1>
        </header>""")
        print(nav)
        print("""        <main>
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
        </main>""")

    # Body para la pagina de contacto

    def body_contacto(nav):
        print(f"""    <body>
        <header>
            <h1>Pagina de contacto</h1>
        </header>""")
        print(nav)
        print("""        <main>
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
        </main>""")


    def body_listado_total_bicis(nav):
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")
        x = 0
        while x <= (len(bikes_json)-1):
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{bikes_json[x]['img']}"></img>
                    <br>"""
                    f"<a href='bikes/{bikes_json[x]['_id']}.html'> <b>""", bikes_json[x]['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", bikes_json[x]['Model']['Name'] ,bikes_json[x]['Model']['Wheel size']['$numberDouble']+'"<br>'
                    ,bikes_json[x]['Price']['$numberInt']+"""€/dia <br>
                </div><br>""")
                x += 1

        print("""            </div>
        </section>""")
    
    # Body para la los tipos de bicis

    def body_listado_tipo_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de tipos de Bicis </h1>
        </header>""")
        print(nav)
        print("""        <section>
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
            enlace = "<a href='types/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
        </section>""")

        
    # Body para las marcas de bicis 

    def body_listado_marca_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de bicis por marca </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")

        x = 0
        marcas_bicis = []
        while x <= (len(bikes_json)-1):

            marca = bikes_json[x]['Brand']

            if marca in marcas_bicis:
                pass
            else:
                marcas_bicis.append(marca)

            x += 1
        
        for x in marcas_bicis:
            enlace = "<a href='brand/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
        </section>""")

    #Body para mostrar las bicis segun su localización

    def body_listado_por_zona_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de Bicis por zona </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")

        x = 0
        zonas_bicis = []
        while x <= (len(bikes_json)-1):

            zonas = bikes_json[x]['Location']

            if zonas in zonas_bicis:
                pass
            else:
                zonas_bicis.append(zonas)

            x += 1
        
        for x in zonas_bicis:
            enlace = "<a href='location/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
        </section>""")


    def body_listado_por_tamaño_rueda_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de Bicis por tamaño de rueda </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")

        x = 0
        tamaño_rueda_bicis = []
        while x <= (len(bikes_json)-1):

            tamaño_rueda = bikes_json[x]['Model']['Wheel size']['$numberDouble']

            if tamaño_rueda in tamaño_rueda_bicis:
                pass
            else:
                tamaño_rueda_bicis.append(tamaño_rueda)

            x += 1
        
        for x in tamaño_rueda_bicis:
            enlace = "<a href='wheelsize/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
        </section>""")

    def body_listado_por_desarollo_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de Bicis por desarollo </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")

        x = 0
        desarrollo_bicis = []
        while x <= (len(bikes_json)-1):

            desarrollo = bikes_json[x]['Model']['Wheel size']['$numberDouble']

            if desarrollo in desarrollo_bicis:
                pass
            else:
                desarrollo_bicis.append(desarrollo)

            x += 1
        
        for x in desarrollo_bicis:
            enlace = "<a href='wheelsize/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
        </section>""")

    
    def body_listado_por_cambio_bicis(nav):
        print("""    <body>
        <header>
            <h1>Listado de Bicis por tipo de cambio </h1>
        </header>""")
        print(nav)
        print("""        <section>
            <div>""")

        x = 0
        cambio_bicis = []
        while x <= (len(bikes_json)-1):

            cambio = bikes_json[x]['Model']['Type']

            if cambio in cambio_bicis:
                pass
            else:
                cambio_bicis.append(cambio)

            x += 1
        
        for x in cambio_bicis:
            enlace = "<a href='wheelsize/{}.html'> {} </a>".format(x,x)
            print("                <div>",enlace ,"</div>")  
        print("""            </div>
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


def paginas_tipos_bicis(nav_2):
    
    diccionarioBicisPorTipos = diccionario_tipos_bicis()
    
    for x in diccionarioBicisPorTipos:

        page ='docs/types/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis tipo {x}', description=f'Pagina de listado de bicis tipo {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPorTipos[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()

def paginas_marcas_bicis(nav_2):
    
    diccionarioBicisPorMarcas = diccionario_marcas_bicis()
    
    for x in diccionarioBicisPorMarcas:

        page ='docs/brand/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis marca {x}', description=f'Pagina de listado de bicis marca {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPorMarcas[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()

def paginas_zonas_bicis(nav_2):
    
    diccionarioBicisPorZonas = diccionario_zonas_bicis()
    
    for x in diccionarioBicisPorZonas:

        page ='docs/location/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis zona {x}', description=f'Pagina de listado de bicis por zona {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPorZonas[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()


def paginas_tamaño_ruedas_bicis(nav_2):
    
    diccionarioBicisPorTamañoRuedas = diccionario_tamaño_ruedas_bicis()
    
    for x in diccionarioBicisPorTamañoRuedas:

        page ='docs/wheelsize/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis con tamaño de rueda {x}', description=f'Pagina de listado de bicis tamaño de rueda {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPorTamañoRuedas[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()
    


def paginas_desarrollo_bicis(nav_2):
    
    diccionarioBicisPordesarrollo = diccionario_desarrollo_bicis()
    
    for x in diccionarioBicisPordesarrollo:

        page ='docs/developments/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis con desarollo {x}', description=f'Pagina de listado de bicis segun su desarollo {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPordesarrollo[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()
    

def paginas_cambio_bicis(nav_2):
    
    diccionarioBicisPorCambio = diccionario_cambios_bicis()
    
    for x in diccionarioBicisPorCambio:

        page ='docs/shifts/'+ x + '.html'
        sys.stdout = open(page,'w',encoding="UTF-8")
        html_head(title=f'Bicis con cambio {x}', description=f'Pagina de listado de bicis segun su tipo de cambio {x}')
        print("""    <body>
        <header>
            <h1> Bicis disponibles </h1>
        </header>""")
        print(nav_2)
        print("""<section>
            <div>""")

        for document in diccionarioBicisPorCambio[x]:
                print(f"""                <div>
                    <img alt="imagen" width='200' height='200' src="{document['img']}"></img>
                    <br>"""
                    f"<a href='../bikes/{document['_id']}.html'> <b>""", document['Brand']  ,"""</b> </a><br>
                    Bicicleta de tipo""", document['Model']['Name']  ,document['Model']['Wheel size']['$numberDouble']+'"',"""<br>
                    """,document['Price']['$numberInt']+"€/dia <br>"
                """
                </div><br>""")


        print("""                </div>
        </section>""")

        footer()
        
        sys.stdout.close()