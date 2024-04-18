 # librerias -->
import typer
import cv2
import os
from resources.imageFunctions import __colorToGray, __imageToPixelart, __pixelsToVectors, __adjustImage
from resources.imageFunctions import __simpleBlurImage, __roundImage, __noiseFilter, __copyrightImage, __rotateImage
from resources.menuFunction import __helpTable, __selectTable
from resources.formatFunctions import __compressImage, __changeFormat, __webOptimizer

LENGTH_OPTIONS = 9;

 # funciones -->
  # funcion - principal =>
def __main():
  os.system('clear')
  print(' --> Traza: La funcion "Main" esta funcionando...')

  __selectTable()
  optionSelected = int(input(' -> Selecciona una opcion valida (omision=1): '))

  if ((optionSelected >= 1) and (optionSelected <= LENGTH_OPTIONS)):
    imageSelected = input(' -> Selecciona la imagen que quieras (/ruta/imagen.png): ')
    switch(optionSelected, imageSelected)
  else:
    os.system('clear')
    typer.run(__helpTable)


  # funcion - switch =>
def switch(argument, imageInput):
  __folderExists("mod-images")

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

#|----------------------------------------------------------------------------------------->
def __folderExists(folderName):
  if not os.path.exists(folderName):
    os.makedirs(folderName)
    print("[bold green]  -> Directorio creado con exito.[/bold green]")

#|----------------------------------------------------------------------------------------->
 # constructor - principal =>
if (__name__ == '__main__'):
  typer.run(__main)