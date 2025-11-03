import cv2 
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img=cv2.line(img,(0,height),(width,0),(0,255,0),5)

    img=cv2.rectangle(img,(100,100),(200,200),(128,128,128),6)

    img=cv2.circle(img,(150,150),50,(0,0,255),6)

    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,"Hello World", (200,height-10),font,1,(0,0,0),2,cv2.LINE_AA)

    cv2.imshow("Frame",img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 