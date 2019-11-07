import cv2
import numpy as numpy

cap = cv2.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("VIDEO",gray)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()