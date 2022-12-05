import typer
from rich import print
import json
from src.crud.main import mongoDBcrud

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
        status = typer.prompt('Introduce disponibildiad (avaliable o rented)')


        print("[blue]Documento a insertar:[/blue]")
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
            
        print(query)
        confirm = typer.confirm("Seguro que quieres insertarlo?")
        if not confirm:
            print("Abortando...")
            raise typer.Abort()
        else:
            mongoDBcrud.create(_id, brand, modelName, modelStyle, modelSuspension, modelMaterial, modelForkBrand, modelForklenght, modelDevelopments, modelGroup, modelType, priceday, status)
    
    else:

        print("Subiendo archivo archivo JSON",'\n')

        with open(jsonFile) as file:
            file_data = json.load(file)

        print(file_data)

        # if isinstance(file_data, list):
        #     Collection.insert_many(file_data)
        # else:
        #     Collection.insert_one(file_data)




@app.command()
def despedir():
    print("Chao pescao!")




if __name__ == '__main__':
    app()