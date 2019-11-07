import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # For naked eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') # For Eyes with glasses.

cap = cv2.VideoCapture(0)

while(True):
    if not cap.isOpened():
        cap.open()
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
           frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h,x:x+h]
           roi_color = frame[y:y+h,x:x+h]
           eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
           for(ex,ey,ew,eh) in eyes:
               cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow("VIDEO",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()