import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,40.0,(640,480))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        cv2.imshow("VIDEO",frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
