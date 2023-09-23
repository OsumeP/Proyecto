import cv2
import os
import face_recognition

#Codificar rostros
imagesFacesPath = "D:/1_OsumeP/UNAL/Proyecto/Test/images/faces"

facesEncodings = []
facesNames = []
for fileName in os.listdir(imagesFacesPath):
    image = cv2.imread(imagesFacesPath + "/" + fileName)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    f_codings = face_recognition.face_encodings(image, known_face_locations=[(0,150,150,0)])[0]
    facesEncodings.append(f_codings)
    facesNames.append(fileName.replace(".jpg", ''))
#################################
#Comparando rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == False: break
    orig = frame.copy()
    faces = faceClassif.detectMultiScale(frame, 1.1, 5)

    for (x, y, w, h) in faces:
        face = orig[y: y+h, x:x+w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        actualFaceEncoding = face_recognition.face_encodings(face, known_face_locations=[(0,w,h,0)])[0]
        result = face_recognition.compare_faces(facesEncodings, actualFaceEncoding)
        if True in result:
            index = result.index(True)
            name = facesNames[index]
            color = (125, 220, 0)
        else:
            name = "Desconocido"
            color = (50, 50, 255)

        cv2.rectangle(frame, (x,y+h), (x + w, y + h + 30), (0, 255, 0), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame,name,(x, y + h + 25), 2, 1, (255, 255, 255), 2, lineType=cv2.LINE_AA)
    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break