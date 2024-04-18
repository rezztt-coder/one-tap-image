 # librerias -->
import cv2
import numpy as np

# /home/rezzt/Imágenes/rzt-images/avatar-images/avatar-11.png
 # funciones -->
  # funcion - colorToGray =>
def __colorToGray(imageInput, imageOutput):
  print(' --> Traza: La funcion "colorToGray" esta funcionando...')

  imageBase = cv2.imread(imageInput)
  imageGray = cv2.cvtColor(imageBase, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(imageOutput, imageGray)

#|--------------------------------------------------------->
  # funcion - imageToPixelart =>
def __imageToPixelart(imageInput, imageOutput):
  print(' --> Traza: La funcion "imageToPixelart" esta funcionando...')

  imageBase = cv2.imread(imageInput)
  pixelFactor = 6
  newHeight, newWidth = imageBase.shape[:2]

  imagePixel = cv2.resize(imageBase, (newWidth // pixelFactor, newHeight // pixelFactor), interpolation=cv2.INTER_NEAREST)
  imagePixel = cv2.resize(imagePixel, (newWidth, newHeight), interpolation=cv2.INTER_NEAREST)

  cv2.imwrite(imageOutput, imagePixel)

#|--------------------------------------------------------->
  # funcion - vectorizedImage =>
def __pixelsToVectors(imageInput, imageOutput):
  print(' --> Traza: La funcion "pixelsToVectors" esta funcionando...')

  imageBase = cv2.imread(imageInput)
  grayScale = cv2.cvtColor(imageBase, cv2.COLOR_BGR2GRAY)
  _, blackWhite = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)

  contours, _ = cv2.findContours(blackWhite, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  vectorizedImage = imageBase.copy()
  cv2.drawContours(vectorizedImage, contours, -1, (0, 255, 0), 2)

  cv2.imwrite(imageOutput, vectorizedImage)

#|--------------------------------------------------------->
  # funcion - adjustBrightnessContrast =>
def __adjustImage(imageInput, imageOutput):
  print(' --> Traza: La funcion "adjustImage" esta funcionando...')

  def __brightnessContrast(imageInput, numBrillo, numContraste):
    """
     - bright > ajusta el valor del brillo (positivo-subir | negativo-bajar)
     - contrast > ajusta el valor del contraste (positivo-subir | negativo-bajar)
    """
    brillo = int(numBrillo)
    contraste = int(numContraste)
    
    newImage = cv2.addWeighted(imageBase, 1 + contraste/127, imageBase, 0, brillo - contraste)
    return newImage

  imageBase = cv2.imread(imageInput)
  adjustImage = __brightnessContrast(imageBase, -30, 20)
  
  cv2.imwrite(imageOutput, adjustImage)

#|--------------------------------------------------------->
  # funcion - simpleBlurImage =>
def __simpleBlurImage(imageInput, imageOutput):
  print(' --> Traza: La funcion "simpleBlueImage" esta funcionando...')
    
  imageBase = cv2.imread(imageInput)
  blurredImage = cv2.GaussianBlur(imageBase, (15,15), 0)

  cv2.imwrite(imageOutput, blurredImage)

#|--------------------------------------------------------->
  # funcion - roundImage =>
def __roundImage(imageInput, imageOutput):
  print(' --> Traza: La funcion "roundImage" esta funcionando...')

  imageBase = cv2.imread(imageInput)
  
  height, width = imageBase.shape[:2]
  imageCenter = (width // 2, height // 2)
  imageRadius = min(width, height) // 2

  imageMask = np.zeros((height, width), dtype=np.uint8)
  cv2.circle(imageMask, imageCenter, imageRadius, 255 , -1)
  circleImage = cv2.bitwise_and(imageBase, imageBase, mask=imageMask)

  cv2.imwrite(imageOutput, circleImage)

#|--------------------------------------------------------->
  # funcion - rotateImage =>
def __rotateImage(imageInput, imageOutput):
  print(' --> Traza: La funcion "rotateImage" esta funcionando...')

#|--------------------------------------------------------->
  # funcion - noiseFilter =>
def __noiseFilter(imageInput, imageOutput):
  print(' --> Traza: La funcion "noiseFilter" esta funcionando...')
  imageBase = cv2.imread(imageInput)

  mean = 0
  stddev = 0.5

  noiseFilter = np.random.normal(mean, stddev, imageBase.shape).astype(np.uint8)
  noiseImage = cv2.add(imageBase, noiseFilter)

  cv2.imwrite(imageOutput, noiseImage)

#|--------------------------------------------------------->
  # funcion - copyrightImage =>
def __copyrightImage(imageInput, imageOutput, textInput):
  print(' --> Traza: La funcion "copyrightImage" esta funcionando...')
  imageBase = cv2.imread(imageInput)
  
  waterMark = textInput
  fontMark = cv2.FONT_HERSHEY_COMPLEX
  fontScale = 1
  fontThickness = 2

  textColor = (255, 255, 255, 100)
  textPosition = (50, 50)

  cv2.putText(imageBase, waterMark, textPosition, fontMark, fontScale, textColor, fontThickness)
  cv2.imwrite(imageOutput, imageBase)