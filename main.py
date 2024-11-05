# from HandTrackingmodule import HandTracking
from VolumeHandControl import VolumeHandControl
import cv2 
import time 
import math


#####################################
wCam,hCam = 640,480

#####################################
if __name__ == "__main__":
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)

    # handTracking = HandTracking()
    VHC = VolumeHandControl()
    while True:
            sucess , img =  cap.read()

            # image = handTracking.Track_Hands(img)
            image = VHC.Change_Volume(img)

            
                     

            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime

            cv2.putText(image,str(int(fps)),(10,70) , cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            cv2.imshow("Image",image)
            cv2.waitKey(1)

    