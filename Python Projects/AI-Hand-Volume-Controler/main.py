import mediapipe as mp

import cv2
import time
class handetector():
    def __init__(self,mode=False,max_num_hands=2,detectionCon=0.5,trackcon=0.8 ):
        self.mode=mode
        self.max_num_hands=max_num_hands
        self.detectionCon= detectionCon
        self.trackCon = trackcon
        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands(self.mode,self.max_num_hands,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
        self.tipIds=[4,8,12,16,20]
    def findhands(self,img,draw=True):
     try:
        imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mphands.HAND_CONNECTIONS)
        return img
     except Exception as p:
            pass

    def fingersup(self):
        fingers=[]
        #thumb
        if self.lmlist[self.tipIds[0]][1]>self.lmlist[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 fingers
        for id in range(0,5):
            if self.lmlist[self.tipIds[id]][2]<self.lmlist[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


    def findpos(self,img,handno=0,draw=True ):
            xlist=[]
            ylist=[]
            bbox=[]
            self.lmlist=[]
            if self.results.multi_hand_landmarks:
                myhand=self.results.multi_hand_landmarks[handno]
                for id,lm in enumerate(myhand.landmark):
                    h,w,c=img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    xlist.append(cx)
                    ylist.append(cy)
                    self.lmlist.append([id,cx,cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 2, (255, 0, 255), cv2.FILLED)
                xmin,ymin=min(xlist)-20, min(ylist)-20
                xmax,ymax= max(xlist)+20,max(ylist)+20
                bbox=xmin,ymin,xmax,ymax
                if draw:
                    cv2.rectangle(img,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,0),2)
            return  self.lmlist,bbox
def main():
    # wcam,hcam=640,480
    cap = cv2.VideoCapture(0)
    # cap.set(3,wcam)
    # cap.set(4,hcam)
    detector=handetector()
    while (1):
      try:
        success, img = cap.read()
        img=detector.findhands(img)
        lmlist,bbox=detector.findpos(img)
        if len(lmlist) !=0:
            print(lmlist[4])
        cv2.imshow("Image", img)
        cv2.waitKey(1)
      except Exception as e:
          pass
if __name__=="__main__":
    main()
