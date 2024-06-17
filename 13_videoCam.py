import cv2 as cv 
import numpy as np 


cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Detect red color in video
    lower_red = np.array([0,50,50])
    upper_red = np.array([6, 255, 180])
    
    mask_red = cv.inRange(frame_hsv, lower_red, upper_red)
    fram_masked = cv.bitwise_and(frame, frame, mask=mask_red)
    
    cv.imshow("frame", frame)
    cv.imshow("mask_red", mask_red)
    cv.imshow("fram_masked", fram_masked)
    
    key_exit = cv.waitKey(5) & 0xff
    if key_exit == 27:
        break
    
cv.destroyAllWindows()
cap.release()