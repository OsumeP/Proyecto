import cv2
import os
import imutils

#Generamos una variable con el nombre de la persona para crear un directorio con ese nombre.
personName = 'Juan David'
dataPath = 'D:/1_OsumeP/UNAL/Programacion/Proyecto/Data'
#Señalamos la ruta en donde se guardarán las imágenes.
personPath = dataPath + '/' + personName

#Si la ruta no existe, se creará.
if not os.path.exists(personPath):
    #Creación del directorio
    os.makedirs(personPath)
    print('Capeta creada', personPath)

#Generamos el objeto que señala que se capturará video en vivo
capture = cv2.VideoCapture(0)
#Creamos un detector de rostros usando clasificadores pre-entrenados porOpenCV
clasificadorFace = cv2.CascadeClassifier(cv2.data.haarcascade + 'haarcascade_frontalface_default.xml')

count = 0
#Ciclo while mientras la cámara esté abierta.
while capture.isOpened():
    confirm, frame = capture.read()
    #Si no lográ capturar la imagen en vivo se rompe el ciclo
    if confirm == False: break
    #Guardamos en una variable el frame en escala de grises
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clasificadorFace.detectMultiScale(grayImg,
                                              #ScaleFactor: Que tanto se reduce la imagen en la pirámide de imágenes.
                                              1.3, 
                                              #minNeighbors: 
                                              5)