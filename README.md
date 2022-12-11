# Booking Bike :biking_man:
Repositorio del proyecto de Diciembre 2022
Enlace del proyecto: https://z0s3r77.github.io/BooKingBikeV2/

**Indice**

- [**Introducción**](#introducción)
- [**Descripción técnica**](#Descripción técnica)
  - [**Arquitectura de la aplicación**](#Arquitectura de la aplicación)


# Introducción 

El proyecto **Booking Bike** tiene como finalidad desplegar un conjunto de páginas sobre bicicletas, obteniendo su contenido a partir de una base de datos, mediante Python.

El sitio Web tiene que simular ser una página de reservas de bicicletas disponibles en Mallorca, Islas Baleares. 

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
- **HTML y CSS**


Cumpliendo con el propósito indicado anteriormente, el proyecto presenta la siguiente **Arquitectura**.

## Arquitectura de la aplicación

A continuación una imagen de la arquitectura:

file:///home/z0s3r77/Descargas/Conceptos%20relacionados(2).jpg![imagen](https://user-images.githubusercontent.com/80277545/206925650-5ab8087a-086a-4726-a586-3b74ef6f80ea.png)


- En primer lugar tenemos la base de datos, donde se almacenan las bicicletas, en concreto en una colección llamada Bikes dentro de la base de datos BookingBike (pero de esto daremos detalles más abajo). 

- Mediante Python en la **capa de acceso a datos**, nos conectamos al cluster de Mongo Atlas mediante la API proporcionada por esta misma. Importamos los datos, los formateamos y los guardamos en documentos **JSON**. A esto lo llamamos **proceso de datos**.

- A continuación , en la **capa lógica** , convertirmos los datos de los archivos JSON en objetos Python y montamos las diferentes páginas con el contenido extraido. Aparte contamos con un programa CRUD, al cuál se puede acceder mediante la terminal CLI.

- Por último, en la **capa de presentación**, servimos las diferentes páginas que se han creado en Github Pages. Por otro lado, proporcionamos la CLI mencionada anteriormente. De ahí viene que desde el punto **TERMINAL CLI** en la imagen superior se pueda volver hacia atrás, ya que está mediante el CRUD servido en la **capa lógica** puede alterar la base de datos. 

## Diagrama de componenetes

file:///home/z0s3r77/Descargas/diagramamodelos.jpg![imagen](https://user-images.githubusercontent.com/80277545/206929865-c167b0b6-b298-4d5f-a247-1de6c2ce781f.png)


