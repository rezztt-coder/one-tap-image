 # libraries -->
import typer
from rich.table import Table
from rich.console import Console

 # functions -->
console = Console()

def __helpTable():
  print(' --> Traza: La funcion "table" esta funcionando...')

   # image table =>
  imageTable = Table(title="HELP COMMANDS - IMAGE FUNCTIONS")
    # image table - create columns =>
  imageTable.add_column("COMMAND")
  imageTable.add_column("DESCRIPTION")
  imageTable.add_column("EXAMPLE")
    # image table - create rows =>
  imageTable.add_row("1. __colorToGray", "Convert a color image to a gray-scale image", "__colorToGray('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("2. __imageToPixelart", "Create a pixelart-image based on a image", "__imageToPixelart('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("3. __pixelsToVectors", "Vectorized a normal image into a vector-image", "__pixelsToVectors('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("4. __adjustImage", "Upgrade the image using the bright and contrast", "__adjustImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("5. __simpleBlurImage", "Apply Gaussian Blur Filter to an image", "__simpleBlurImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("6. __roundImage", "Create a rounded image like profile image", "__roundImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("7. __rotateImage", "Rotate a Image with the angles you want", "__rotateImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("8. __noiseFilter", "Apply Noise Filter to an image", "__noiseFilter('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  imageTable.add_row("9. __copyrightImage", "Apply a WaterMark to an image", "__copyrightImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png', 'texto-ejemplo')")
  
  console.print(imageTable)

  #|========================================================>>
   # format table =>
  formatTable = Table(title="HELP COMMANDS - FORMAT FUNCTIONS")
    # format table - create columns =>
  formatTable.add_column("COMMAND")
  formatTable.add_column("DESCRIPTION")
  formatTable.add_column("EXAMPLE")
    # format table - create rows =>
  formatTable.add_row("1. __compressImage", "Compress an image reducing quality", "__compressImage('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")
  formatTable.add_row("2. __changeFormat", "Change the format of an image", "__changeFormat('ruta/imagenInput.png', '/ruta/ImagenOutput.png'), '.formato'")
  formatTable.add_row("3. __webOptimizer", "Optimize an image to using into a Web", "__webOptimizer('ruta/imagenInput.png', '/ruta/ImagenOutput.png')")

  console.print(formatTable)

#|------------------------------------------------------------------------>
def __selectTable():
  print(' --> Traza: La funcion "selectTable" esta funcionando...')

  selectTable = Table(title="SELECTION - TABLE")
  selectTable.add_column("OPTION", justify="center")
  selectTable.add_column("DESCRIPTION", justify="full")

  selectTable.add_row("1", "IMAGES - FUNCTIONS | List of functions to manipulate images")
  selectTable.add_row("2", "FORMAT - FUNCTIONS | List of functions to formar images")
  console.print(selectTable)

#|------------------------------------------------------------------------>
def __selectTableImage():
  print(' --> Traza: La funcion "selectTableImage" esta funcionando...')

   # selection table =>
  selectTableImage = Table(title="OPTIONS LIST - TABLE")
    # selection table - create columns =>
  selectTableImage.add_column("OPTION", justify="center")
  selectTableImage.add_column("COMMAND", justify="full")
    # selection table - create rows =>
  selectTableImage.add_row("1", "Convert to Gray Scale > __colorToGray")
  selectTableImage.add_row("2", "Create Pixelart > __imageToPixelart")
  selectTableImage.add_row("3", "Transform pixel-image to vector-image > __pixelsToVector")
  selectTableImage.add_row("4", "Upgrade the image view > __adjustImage")
  selectTableImage.add_row("5", "Applies Gaussian Blur filter > __simpleBlurImage")
  selectTableImage.add_row("6", "Create a rounded image like profiles > __roundImage")
  selectTableImage.add_row("7", "Rotate image in diferents angles > __rotateImage")
  selectTableImage.add_row("8", "Applies Noise Filter > __noiseFilter")
  selectTableImage.add_row("9", "Applies a WaterMark to a Image > __copyrightImage")
  console.print(selectTableImage)

#|------------------------------------------------------------------------>
