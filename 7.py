import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_cascade.empty():
        raise IOError('xml not found')
cap = cv2.VideoCapture('video2.mp4')
scalling_factor = 0.5
while True:
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx = scalling_factor, fy = scalling_factor, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('Face Detection',frame)
    if cv2.waitKey(33) == 27: 
        break
cv2.destroyAllWindows()   
