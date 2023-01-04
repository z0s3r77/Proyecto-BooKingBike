# Booking Bike :biking_man:
Repositorio del proyecto de Diciembre 2022
Enlace del proyecto: https://z0s3r77.github.io/BooKingBikeV2/

**Indice**

- [**Introducción**](#introducción)
- [**Descripción técnica**](#descripción-técnica)
  - [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
  - [**Diagrama de componentes**](#diagrama-de-componentes)
- [**Clockify**](#clockify)
- [**Pytest**](#Pytest)

# Introducción 

El proyecto **Booking Bike** tiene como finalidad desplegar un conjunto de páginas sobre bicicletas, obteniendo su contenido a partir de una base de datos, mediante Python.

El sitio Web tiene que simular ser una página en la cual diferentes organizaciones pueden añadir sus bicicletas disponibles en Mallorca, Islas Baleares.
Entonces el cliente al seleccionar la bici deseada le enviaria a la pagina web del anunciante.

Las tecnologías que se han utilizado han sido las siguientes:

- En la base de datos, se ha utilizado [**MongoDB**](https://www.mongodb.com), mediante un clúster en Mongo Atlas.
- El lenguaje de programación elegido ha sido [**Python**](https://www.python.org/) en su  versión 3.8.
- Como servidor web para mostrar las páginas se ha utilizado el que proporciona Github mediante Pages.

# Descripción técnica

En este apartado procedemos a detallar mediante tecnicismos como funciona el proyecto.
Dado que los usuarios a usar son dos, un técnico y un usuario sin conocimientos. El técnico debe tener acceso a una interfaz de consola (CLI) para poder realizar un CRUD a la base de datos de Booking Bike, es decir, crear, leer, actualizar y borrar documentos. Por otro lado, estaría el usuario que quiere reservar la bicicleta, este tan solo tendría acceso a la VISTA del proyecto, es decir, a la página que se despliega en Github Pages.

## Tecnologías usadas

Para poder llevar a cabo el proyecto se han utilizado las siguientes técnologias:

- **Python**
- **MongoDB**
- **Git**
- **Github Pages**
- **HTML**
- **CSS responsive para Ordenador, iPhone XR y IPad Air**


Cumpliendo con el propósito indicado anteriormente, el proyecto presenta la siguiente **Arquitectura**.

## Arquitectura de la aplicación

A continuación una imagen de la arquitectura:

![imagen](https://user-images.githubusercontent.com/80277545/206925650-5ab8087a-086a-4726-a586-3b74ef6f80ea.png)


- En primer lugar tenemos la base de datos, donde se almacenan las bicicletas, en concreto en una colección llamada Bikes dentro de la base de datos BookingBike (pero de esto daremos detalles más abajo). 

- Mediante Python en la **capa de acceso a datos**, nos conectamos al cluster de Mongo Atlas mediante la API proporcionada por esta misma. Importamos los datos, los formateamos y los guardamos en documentos **JSON**. A esto lo llamamos **proceso de datos**.

- A continuación , en la **capa lógica** , convertirmos los datos de los archivos JSON en objetos Python y montamos las diferentes páginas con el contenido extraido. Aparte contamos con un programa CRUD, al cuál se puede acceder mediante la terminal CLI.

- Por último, en la **capa de presentación**, servimos las diferentes páginas que se han creado en Github Pages. Por otro lado, proporcionamos la CLI mencionada anteriormente. De ahí viene que desde el punto **TERMINAL CLI** en la imagen superior se pueda volver hacia atrás, ya que está mediante el CRUD servido en la **capa lógica** puede alterar la base de datos. 

## Diagrama de componentes

![imagen](https://user-images.githubusercontent.com/80277545/207053951-2394eceb-e8a9-421d-a0fd-9d5f03d4c780.png)



En el este diagrama se indica el flujo de trabajo del Programa. El diagrama empieza con el modulo de TYPER_main.py, que despliega una CLI para poder desplegar el site o interactuar con el CRUD.

Por este motivo modulo TYPER_main.py se divide en VIEWS y CRUD. Cuando se quiere lanzar el CRUD se despliega mediante TYPER una CLI que en el cual se indican las operaciones que se pueden hacer:

![imagen](https://user-images.githubusercontent.com/80277545/206933144-84d09b78-e67d-43a5-9c03-a0e9aab22bec.png)

Por otro lado, si desplegamos el site, seguiriamos el otro flujo, el de VIEWS_main.py y se ejecutarían todos los modulos de abajo arriba.

## Librerias utilizadas

Para poder llevar a acabo el proyecto se han utilizado las siguientes librerias en Python:

  - `PyMongo`: Se ha utilizado para poder lanzar comandos de MongoDB desde Python hacia el cluster de Mongo Atlas.
  - `Typer`: Se ha utilziado para poder montar y desplegar la CLI con una interfaz comoda y ligera.
  - `PyTest`: Se ha utilizado para poder realizar casos test sobre los distintos modulos del proyecto.
  - `Coverage`: Se ha utilizado para poder ver, con la ayuda de Pytest la cobertura de los test sobre todo los modulos. Dato curioso, es de 91%
  - `Requests`: Se ha utilizado para poder realizar una petición HTTP a la API de Mongo Atlas.
  - `Schema`: Se ha utilizado para, mediante Python poder comprobar una estructura JSON.

# Clockify

![imagen](https://user-images.githubusercontent.com/80277545/207130055-abff2951-d326-480e-9cc3-e674b793ee27.png)

# Pytest 

Para ejecutar los test se debe seguir la estructura puesta en `pytest.ini`, por otro lado , se pueden ejecutar todos los tets con el siguiente comando: 
```
coverage run -m pytest -vv test/test_VIEW_main.py test/test_DB_conexionApiMongo.py test/test_DB_MongoAtlasConexion.py test/test_DB_generadorJson.py test/test_DB_convertirJsonALista.py test/test_DB_mainDB.py  test/test_CRUD_main.py
```

El comando anterior ejecutaria el Pytest bajo coverage. 
![imagen](https://user-images.githubusercontent.com/80277545/207448219-f454d6ca-a8f3-4a70-a937-e06ddad95702.png)

