# pip install mediapipe, pip install cvzone
import cv2 as cv 
import numpy as np
from cvzone.HandTrackingModule import HandDetector



cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)


while(True):
    rec, frame = cap.read()
    hand,img = detector.findHands(frame)
    
    if hand :
        hand1 = hand[0]
        lmlist1 = hand1['lmList']
        length, info, frame = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], frame)
        
    cv.imshow('frame', frame)
    key_exit = cv.waitKey(5) & 0xff
    if key_exit == 27:
        break

cv.destroyAllWindows()
cap.release()
