
import mediapipe as mp
import cv2
import main as hp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,180)
detector=hp.handetector(detectionCon=0.7, max_num_hands=1)

#pycaw module
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volrange=volume.GetVolumeRange()

# minvol=volrange[0]
# maxvol=volrange[1]
volbar=400
volper=0
area=0




while True:
    success,img=cap.read()

    img=detector.findhands(img)
    lmlist,bbox=detector.findpos(img,draw=True)

    if len(lmlist) !=0:
        # Filter based on size
        area = (bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        # print(lmlist[4],lmlist[8])      #hand points value
        length = math.hypot(lmlist[8][1] - lmlist[4][1], lmlist[8][2] - lmlist[4][2])  # length of line
        if 250<area<1500:

            cv2.circle(img, (lmlist[4][1], lmlist[4][2]), 15, (255, 0, 255), cv2.FILLED)    #draw circles
            cv2.circle(img, (lmlist[8][1], lmlist[8][2]), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img,(lmlist[4][1], lmlist[4][2]),(lmlist[8][1], lmlist[8][2]),(255,0,255),3)   #draw line

            cx,cy= (lmlist[8][1] + lmlist[4][1]) //2 ,(lmlist[8][2]+lmlist[4][2])//2    #find center of line
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)                           #circle on mid line


            # print("yes")
            # vol = np.interp(length, [50, 300], [minvol, maxvol])
            # volume.SetMasterVolumeLevel(vol, None)

            volper= np.interp(length, [50,200], [0,100])
            volbar = np.interp(length, [50, 200], [400, 150])


            # reduce resolution
            smoothness=5
            volper = smoothness*round(volper/smoothness)

            # #check finger up
            fingers=detector.fingersup()
            if not fingers[5]:
                volume.SetMasterVolumeLevelScalar(volper / 100, None)
                cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED)


        cv2.rectangle(img, (50,150), (85,400),(0,255,0), 3)
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volper)+1} %', (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)
        currentvol=int(volume.GetMasterVolumeLevelScalar()*100)
        cv2.putText(img, f'Volume: {int(currentvol)} ', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)


    cv2.imshow("Image",img)
    cv2.waitKey(1)