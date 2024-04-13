 # libraries -->
import typer
from rich.table import Table
from rich.console import Console

 # functions -->
console = Console()

def __helpTable():
  print(' --> Traza: La funcion "table" esta funcionando...')

   # image table =>
  imageTable = Table(title="HELP COMMANDS - TABLE")
    # image table - create columns =>
  imageTable.add_column("COMMAND")
  imageTable.add_column("DESCRIPTION")
  imageTable.add_column("EXAMPLE")
    # image table - create rows =>
  imageTable.add_row("__colorToGray", "Convert a color image to a gray-scale image", "__colorToGray('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("__imageToPixelart", "Create a pixelart-image based on a image", "__imageToPixelart('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("__pixelsToVectors", "Vectorized a normal image into a vector-image", "__pixelsToVectors('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("__adjustImage", "Upgrade the image using the bright and contrast", "__adjustImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  console.print(imageTable)

#|------------------------------------------------------------------------>
def __selectTable():
  print(' --> Traza: La funcion "selectTable" esta funcionando...')

   # selection table =>
  selectionTable = Table(title="OPTIONS LIST - TABLE")
    # selection table - create columns =>
  selectionTable.add_column("OPTION", justify="center")
  selectionTable.add_column("COMMAND", justify="full")
    # selection table - create rows =>
  selectionTable.add_row("1", "Convert to Gray Scale > __colorToGray")
  selectionTable.add_row("2", "Create Pixelart > __imageToPixelart")
  selectionTable.add_row("3", "Transform pixel-image to vector-image > __pixelsToVector")
  selectionTable.add_row("3", "Upgrade the image view > __adjustImage")
  console.print(selectionTable)

#|------------------------------------------------------------------------>
