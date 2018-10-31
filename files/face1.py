import numpy as np
import cv2
import time
import requests


def TakeSnapshotAndSave():
    # access the IPcam (every IPcam has a uri)
    cap = cv2.VideoCapture('rtsp://username:password@xx.xx.xx.xx:554/1')
    
    num = 0
    while num<1:
        ret, img = cap.read()
        #cv2.imwrite('opencv'+str(num)+'.jpg',frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img,'Time:'+time.strftime("%c"),(0,450), font, 1,(255,255,255),2)
        cv2.imwrite('face1.jpg',img)
        print ("click")
        
        num = num+1
        

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    TakeSnapshotAndSave()