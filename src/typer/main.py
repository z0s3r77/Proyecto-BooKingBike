import typer
from rich import print
import json
from src.crud.main import mongoDBcrud
from rich.progress import Progress, SpinnerColumn, TextColumn

app = typer.Typer(help="La CLI de BookingBike")

@app.command()
def insertar_documento(jsonFile: str = typer.Option("", help="Inserta un documento JSON directamente")):
    """
    Insertar nuevo documento en la base de datos de MongoAtlas
    """
    if not jsonFile:

        print("Formulario: ")
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


        print("[blue]Documento a insertar:[/blue]",'\n')
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
    
    else:
        print("Subiendo archivo archivo JSON",'\n')
        mongoDBcrud.insert_json(jsonFile)


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
    
        for x in result:
            print(x)

    else:

        _id = typer.prompt("Indica el id del documento")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        )as progress:
            progress.add_task(description="Procesando...", total=None)
            result = mongoDBcrud.read(_id)

        print(result)






if __name__ == '__main__':
    app()