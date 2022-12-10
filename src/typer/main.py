import typer
from rich import print
import json
from src.crud.main import mongoDBcrud
from rich.progress import Progress, SpinnerColumn, TextColumn
import os

app = typer.Typer(help="La CLI de BookingBike te permite realizar un CRUD sobre la colección Bikes de la base de datos BookingBike, ubicada en Mongo Atlas")

@app.command()
def desplegar_site():
    """
    Ejecuta el modulo main de SRC/VIEWS que despliega todo el SITE
    """
    with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    transient=True,
    )as progress:
        progress.add_task(description="Desplegando site...", total=None)
        import src.views.main

    print("[blue] Site Desplegado [/blue]")
    confirm = typer.confirm("Quieres ir al dominio?")
    if confirm:
        typer.launch("file:///home/z0s3r77/Documentos/BooKingBikeV2/docs/home.html")
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

        print("Campos del documento: ")
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
        priceday = typer.prompt('Introduce el precio por día ')
        status = typer.prompt('Introduce disponibildiad (avaliable o rented)','\n')


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
                    "Type": modelType
                },
                "Price": priceday,
                "Status": status
            }
            
        print(query,'\n')

        #Pedimos confirmación, en caso de confirmar, pasa las variables a mongoDBcrud.create
        #Posteriormente hace un read del documento

        confirm = typer.confirm("Seguro que quieres insertarlo?")
        print('\n')
        if not confirm:
            print("Abortando...")
            raise typer.Abort()
        else:
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    transient=True,
                ) as progress:
                progress.add_task(description="Insertando...", total=None)
                mongoDBcrud.create(_id, brand, modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, priceday, status)

            print("[blue]Mostrando documento....[/blue]")
            result = mongoDBcrud.read(_id)
            print(result)
    

    #En caso de usar el parametro jsonFile, enviará el nombre del documento a la función mongoDBcrud.insert_json
    else:

        print("[blue]Comprobando ruta... [/blue]")
        if os.path.exists(jsonFile) == True:
            print(mongoDBcrud.insert_json(jsonFile))
        else:
            print(f"[red]No existe el archivo en la ruta especificada: {jsonFile} [/red]")




@app.command()
def listar_documento(todos: bool = typer.Option(False, help='Mostrar todos los documentos disponibles')):
    """
    Muestra todos los documentos disponibles en la colección Bikes de la base de datos BookingBikes
    """
    if todos:

        print("[blue]Listando todos los documentos[/blue]",'\n')
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        )as progress:
            progress.add_task(description="Procesando...", total=None)
            result = mongoDBcrud.readall()
    
        if result == False:
            result = f'[red]No se han encontrado documentos[/red]'
            print(result)
        
        else:
            contador = 0
            for x in result:
                print(x)
                contador += 1

            print(f"[blue]Estos son todos los resultados: {contador} documentos[/blue]")
            print("[blue]Finalizado con exito[/blue]")

    else:

        _id = typer.prompt("Indica el id del documento")
        # _id = "B5"
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        )as progress:
            progress.add_task(description="Procesando...", total=None)
            result = mongoDBcrud.read(_id)

            if result == False:
                result = f'[red]No existe ningún documento con ID:[/red]  {_id}'
                print(result)
                return False
            else:
                print(result)
                print("finalizado")




@app.command()
def actualizar_documento():

    """
    Actualizar un campo en concreto de un documento proporcionando el ID
    """
    
    targetId = typer.prompt("Indica el ID del documento a actualizar ")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )as progress:
        progress.add_task(description="Buscando documento...", total=None)
        result = mongoDBcrud.read(targetId)
        print(result)

    field = typer.prompt("Indica el campo a actualizar ")
    value = typer.prompt("Indica el nuevo valor")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )as progress:
        progress.add_task(description="Actualizando documento...", total=None)  
        mongoDBcrud.update(targetId, field, value)
        progress.add_task(description="Mostrando resultado...", total=None)
        result = mongoDBcrud.read(targetId)
        print(result)




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




@app.command()
def mostrar_site():
    """
    Inicia el navegador con la pagina principal de BookingBike
    """
    typer.launch("https://bikesbooking.com/es/")



if __name__ == '__main__':
    app()