 # librerias -->
import typer
import cv2
import os
from rich import print
from resources.imageFunctions import __colorToGray, __imageToPixelart, __pixelsToVectors, __adjustImage
from resources.imageFunctions import __simpleBlurImage, __roundImage, __noiseFilter, __copyrightImage, __rotateImage
from resources.menuFunction import __helpTable, __selectTableImage, __selectTable
from resources.formatFunctions import __compressImage, __changeFormat, __webOptimizer

LENGTH_IMAGE_OPTIONS = 9
LENGTH_FUNCT_OPTIONS = 2

 # funciones -->
  # funcion - principal =>
def __main():
  os.system('clear')
  print(' --> Traza: La funcion "Main" esta funcionando...')

  __selectFunctions()

 #|========================================================>>
  # funcion - selectFunctions =>
def __selectFunctions():
  __selectTable()

  optionSelected = int(input(" --> Selecciona una opcion (omision=1): "))
  __validOptions(optionSelected, LENGTH_FUNCT_OPTIONS)
  
  if (__validOptions(optionSelected, LENGTH_FUNCT_OPTIONS) == 1):
    os.system('clear')
    __selectTableImage()

    imageOptionSelected = int(input(" --> Selecciona una opcion (omision=1): "))
    if (__validImageOptions(imageOptionSelected) == True):
      imageSelected = input(" --> Introduce la ruta absoluta de una imagen: ")
      __imageSwitch(imageOptionSelected, imageSelected)

  elif (__validOptions(optionSelected, LENGTH_FUNCT_OPTIONS) == 2):
    os.system('clear')
    print('[bold yellow] => La opcion elegida es "formatFunctions".')


#|----------------------------------------------------------------------------------------->
  # funcion - switch =>
def __imageSwitch(argument, imageInput):
  __folderExists("mod-images", "format-images")

  if (argument == 1):
    __colorToGray(imageInput, 'mod-images/gray-image.png')
  elif (argument == 2):
    __imageToPixelart(imageInput, 'mod-images/pixel-image.png')
  elif (argument == 3):
    __pixelsToVectors(imageInput, 'mod-images/vector-image.png')
  elif (argument == 4):
    __adjustImage(imageInput, 'mod-images/better-image.png')
  elif (argument == 5):
    __simpleBlurImage(imageInput, 'mod-images/blur-image.png')
  elif (argument == 6):
    __roundImage(imageInput, 'mod-images/profile-image.png')
  elif (argument == 7):
    __rotateImage(imageInput, 'mod-images/rotate-image.png')
  elif (argument == 8):
    __noiseFilter(imageInput, 'mod-images/noisy-image.png')
  elif (argument == 9):
    __copyrightImage(imageInput, 'mod-images/copyright-image.png', 'marca-prueba')


  # funcion - folderExists =>
def __folderExists(folderNameImage, folderNameFormat):
  if not os.path.exists(folderNameImage):
    os.makedirs(folderNameImage)
    print("[bold green]  -> Directorio 'mod-images' creado con exito.[/bold green]")

  if not os.path.exists(folderNameFormat):
    os.makedirs(folderNameFormat)
    print("[bold green]  -> Directorio 'format-images' creado con exito.[/bold green]")


  # funcion - validOption =>
def __validOptions(optionInput, numOptions):
  if ((optionInput < 1) or (optionInput > numOptions)):
    os.system('clear')
    __helpTable()
  else:
    return optionInput
  
def __validImageOptions(optionInput):
  if ((optionInput < 1) or (optionInput > LENGTH_IMAGE_OPTIONS)):
    os.system('clear')
    __helpTable()
  else:
    return True


#|----------------------------------------------------------------------------------------->
 # constructor - principal =>
if (__name__ == '__main__'):
  typer.run(__main)