import cv2
import os

#Generamos una variable con el nombre de la persona para crear un directorio con ese nombre.
personName = 'Juan David'
dataPath = 'D:/1_OsumeP/UNAL/Programacion/Proyecto/Data'
#Señalamos la ruta en donde se guardarán las imágenes.
personPath = dataPath + '/' + personName

#Si la ruta no existe, se creará.
if not os.path.exists(personName):
    #Creación del directorio
    os.makedirs(personName)
    print('Capeta creada', personName)

#Generamos el objeto que señala que se capturará video en vivo
capture = cv2.VideoCapture(0)
#Creamos un detector de rostros usando clasificadores pre-entrenados porOpenCV
clasificadorFace = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0
#Ciclo while mientras la cámara esté abierta.
while capture.isOpened():
    confirm, frame = capture.read()
    #Si no lográ capturar la imagen en vivo se rompe el ciclo
    if confirm == False: break
    #Guardamos en una variable el frame en escala de grises
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # #En esta variable vamos a guardar una lista de coordenadas que corresponden a la ubicación del rostro
    faces = clasificadorFace.detectMultiScale(grayImg,
                                               #ScaleFactor: Que tanto se reduce la imagen en la pirámide de imágenes.
                                               1.05, 
                                               #minNeighbors: Cantidad de rectangulo para que se capture un rostro
                                               4)
    #Si el usuario presiona ESC se cerrará la ventana del video en vivo.
    order = cv2.waitKey(1)
    if order == 27:
        break
    for (x,y,w,h) in faces:
        #Dibujo del rectangulo
        cv2.rectangle(frame, 
                      #Punto inicial
                      (x,y),
                      #Punto final
                      (x+w,y+h),
                      #Color
                      (128,0,255),
                      #grosor
                      2)
        if order == ord('s'):
             #Se recorta el rostro del frame
            rostro = frame[y:y+h,x:x+w]
            #Se redimensiona la imagen al quedar guardada en el directorio
            rostro = cv2.resize(rostro,(150,150), cv2.INTER_CUBIC)
            #Se guarda la imagen en el directorio de la persona
            cv2.imwrite(personName + f'/rostro_{count}.jpg', rostro)
            cv2.imshow('rostro', rostro)
            count += 1
    cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
    cv2.putText(frame,'Presione s para almacenar el rostro encontrado',(10,20),2,0.5,(128,0,0),1)
    cv2.imshow('frame',frame)
capture.release
cv2.destroyAllWindows()