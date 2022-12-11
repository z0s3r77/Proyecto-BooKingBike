# Booking Bike :biking_man:
Repositorio del proyecto de Diciembre 2022
Enlace del proyecto: https://z0s3r77.github.io/BooKingBikeV2/

**Indice**

- [Introducción](#introducción)
- [Descripción técnica](#Descripción técnica)


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

Cumpliendo con el propósito indicado anteriormente, el proyecto presenta la siguiente **Arquitectura**.

## Arquitectura de la aplicación

A continuación una imagen de la arquitectura:

Imagen[imagen](https://user-images.githubusercontent.com/80277545/206922964-d7fb27f6-3e1e-47f7-9f3d-c758f5bbeeb7.png)


