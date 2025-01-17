import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

if face_cascade.empty():
        raise IOError('face xml not found')
        if eye_cascade.empty():
            raise IOError('eye xml not found')
cap = cv2.VideoCapture('video4.mp4')
scalling_factor = 0.5
while True:
    ret, frame = cap.read() 
    frame = cv2.resize(frame, None, fx = scalling_factor, fy = scalling_factor, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('Eye Detection',frame)
    if cv2.waitKey(33) == 27: 
        break
cap.release()
cv2.destroyAllWindows()   
