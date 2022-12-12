#Modulo PRINCIPAL de Typer
import typer
from rich import print
from src.crud.main import mongoDBcrud
from rich.progress import Progress, SpinnerColumn, TextColumn
import os

#Se inicia la aplicación de Typer
app = typer.Typer(help="La CLI de BookingBike te permite realizar un CRUD sobre la colección Bikes de la base de datos BookingBike, ubicada en Mongo Atlas")


#Con app.command indicamos los comandos que nos saldrán en la CLI
@app.command()
def desplegar_site():
    """
    Ejecuta el modulo main de SRC/VIEWS que despliega todo el SITE
    """

    #Estos procesos son de la libreria RICH, muestran de forma elegante una barrita cargando.
    with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    transient=True,
    )as progress:
        progress.add_task(description="Desplegando site...", total=None)

        #Importamos el modulo src.views.main, para que se active.Este despliega el site.
        import src.views.main

    print("[blue] Site Desplegado [/blue]")

    #Confirm muestra un prompt, que en caso de Y , muestra la pagina.
    confirm = typer.confirm("Quieres ir al dominio?")
    if confirm:
        typer.launch("file:///home/z0s3r77/Documentos/BooKingBikeV2/docs/index.html")
        print("[blue] Proceso finalizado [/blue]")
        quit()
    else:
        print("[blue]Proceso finalizado[/blue]")





#Comandos que se veran reflejados en la CLI mediante Typer
@app.command()
#La funcion permite insertar un documento fila por fila en la colección Bikes
#También permite, mediante el parametro jsonFile subir directamente un archivo JSON
def insertar_documento(jsonFile: str = typer.Option("", help="Inserta un documento tipo JSON directamente (especifica la ruta)")):
    """
    Insertar nuevo documento en la base de datos de MongoAtlas
    """

    #En caso de no usar opcion jsonFile
    if not jsonFile:

        print("[blue]Campos del documento:[/blue] ")
        _id = typer.prompt('Introduce un id ')
        brand = typer.prompt('Introduce una brand ')
        modelName = typer.prompt('Introduce el tipo de Bicicleta ')
        modelStyle = typer.prompt('Introduce el estilo de Bicicleta ')
        modelSuspension = typer.prompt('Introduce el tipo de suspencion ')
        modelMaterial = typer.prompt('Introduce el material de la bicicleta ')
        modelForkBrand = typer.prompt('Introduce la marca del Fork ')
        modelForklenght = typer.prompt('Introduce la longitud del Fork ')
        modelDevelopments = typer.prompt('Introduce el tipo de desarrollos ')
        modelGroup = typer.prompt('Introduce grupo ')
        modelType = typer.prompt('Introduce de que tipo es la bicicleta(manual o automatica) ')
        modelWheelSize = typer.prompt('Introduce el tamaño de la rueda')
        modelWeight = typer.prompt('Introduce el peso de la bicicleta')
        priceday = typer.prompt('Introduce el precio por día ')
        status = typer.prompt('Introduce disponibildiad (avaliable o rented)','\n')
        location = typer.prompt('Introduce la localización de la bicicleta')
        img = typer.prompt('Introduce la dirección URL de la imagen de la bicicleta')

        print("[blue]Previsualización del documento a insertar:[/blue]",'\n')
        query = {
                "_id" : _id,
                "Brand": brand,
                "Model" : {
                    "Name": modelName,
                    "Style": modelStyle,
                    "Suspension": modelSuspension,
                    "Material": modelMaterial,
                    "Fork brand": modelForkBrand,
                    "Fork length": modelForklenght,
                    "Developments": modelDevelopments,
                    "Group": modelGroup,
                    "Type": modelType,
                    "Wheel size": int(modelWheelSize),
                    "Weight": modelWeight
                },
                "Price": priceday,
                "Status": status,
                "Location": location,
                "img": img
            }
            
        print(query,'\n')

        #Pedimos confirmación, en caso de confirmar, pasa las variables a mongoDBcrud.create
        #Posteriormente hace un read del documento

        confirm = typer.confirm("Seguro que quieres insertarlo?")
        print('\n')
        if not confirm:
            print("[red]Se ha abortado el proceso[/red]")
            quit()
        else:
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    transient=True,
                ) as progress:
                progress.add_task(description="Insertando...", total=None)
                result = mongoDBcrud.create(_id,brand,modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, modelWheelSize, modelWeight, priceday, status, location, img)

            if result == False:
                print("[red]No se ha podido insertar el documento[/red]\n")

            elif result == True:

                print("[blue]Mostrando documento....[/blue]")
                result = mongoDBcrud.read(_id)
                print(result)
                print("[blue]Se ha insertado con exito[/blue]")
    

    #En caso de usar el parametro jsonFile, enviará el nombre del documento a la función mongoDBcrud.insert_json
    else:
        #Comprueba la ruta 
        print("[blue]Comprobando ruta... [/blue]")
        if os.path.exists(jsonFile) == True:
            #Comprobamos la respuesta del metodo insert_json
            if mongoDBcrud.insert_json(jsonFile) == True:
                print("[blue]Se han insertado todos los documentos[/blue]")
            else:
                print("[red] Algo ha ido mal")
        else:
            print(f"[red]No existe el archivo en la ruta especificada: {jsonFile} [/red]")



#Listar documentos hace un print de luna bici indicada por ID.
#La opción de todos, muestra todos los documentos.
@app.command()
def listar_documento(todos: bool = typer.Option(False, help='Mostrar todos los documentos disponibles')):
    """
    Muestra todos los documentos disponibles en la colección Bikes de la base de datos BookingBikes
    """

    #todos, hace referencia al paramtro todos
    if todos:
        print("[blue]Listando todos los documentos[/blue]",'\n')
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        )as progress:
            progress.add_task(description="Procesando...", total=None)
            #result , guarda la respuesta del metodo readall del modulo mongoDBcrud, está es False o la respuesta
            result = mongoDBcrud.readall()
    
        if result == False:
            #Este print no se puede provocar porque es en caso de que no hayan documentos en la colección
            result = f'[red]No se han encontrado documentos[/red]'
            print(result)
        
        else:
            #Esto es en caso de que nos devuelva la respuesta, mostramos los documentos de la respuesta y hacemos un contador
            contador = 0
            for x in result:
                print(x)
                contador += 1

            print(f"[blue]Estos son todos los resultados: {contador} documentos[/blue]")
            print("[blue]Finalizado con exito[/blue]")

    else:

        #En caso de que no se seleccione la opción de todos, pide el id de un documento
        _id = typer.prompt("Indica el id del documento")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        )as progress:
            progress.add_task(description="Procesando...", total=None)
            #Realiza la misma funcion que readall, pero solo con un ID
            result = mongoDBcrud.read(_id)
            
            #Si el resultado es True, sale el documento
            if result == False:
                result = f'[red]No existe ningún documento con ID:[/red]  {_id}'
                print(result)
                return False
            else:
                print(result)
                print("[blue]finalizado[/blue]")



#Comando que actualiza un documento indicando el ID, el campo a modificar y el nombre
@app.command()
def actualizar_documento():

    """
    Actualizar un campo en concreto de un documento proporcionando el ID
    """
    #Pedimos el ID 
    targetId = typer.prompt("Indica el ID del documento a actualizar ")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )as progress:
        progress.add_task(description="Buscando documento...", total=None)
        
        #Ejecutamos un read, mostrado anteriormente
        if mongoDBcrud.read(targetId) == False:
            print("[red]No hay ningún documento con ese ID[/red]")
            quit()

    #Pedimos los campos de FIELD y el VALOR
    field = typer.prompt("Indica el campo a actualizar ")
    value = typer.prompt("Indica el nuevo valor")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )as progress:
        progress.add_task(description="Actualizando documento...", total=None)  
        
        #Enviamos los valores a la función de mongoDBcrud.update, si nos devuelve False
        #Indicamos que no se ha podido actualizar
        if mongoDBcrud.update(targetId, field, value) == False:
            print("[red]No se ha podido actualizar el documento[/red]")
            quit()
        else:
        
        #Por otro lado, si la respuesta de la funcion update es TRUE,
        #Hacemos un print del resultado 
            print("[blue]Documento actualizado[/blue]")
            progress.add_task(description="Mostrando resultado...", total=None)
            result = mongoDBcrud.read(targetId)
            print(result)
            print("[blue]Proceso finalizado[/blue]")




#El comando borrar_documento, obtiene un ID y lo borra.
#En caso de no poder borrarlo, el result se convierte en un mensaje de Error
@app.command()
def borrar_documento():
    """
    Eliminar documento indicando el ID correspondiente
    """
    _id = typer.prompt("Indica el ID del documento que se debe borrar")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )as progress:
        progress.add_task(description="Borrando documento...", total=None) 
        result = mongoDBcrud.delete(_id)
        
    print(result)



#Este comando solo hace un launch de nuestra pagina de GitHub
@app.command()
def mostrar_site():
    """
    Inicia el navegador con la pagina principal de BookingBike
    """
    typer.launch("https://z0s3r77.github.io/BooKingBikeV2/")



if __name__ == '__main__':
    app()