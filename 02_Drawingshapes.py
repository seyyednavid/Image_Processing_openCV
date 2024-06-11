import numpy as np 
import cv2 as cv 

img = cv.imread('./img/navidPic.jpg', cv.IMREAD_COLOR)

"""
# Draw a line
cv.line(img, (5,5), (200,150), (200,100,0), 10)
# Draw a rectangle
cv.rectangle(img, (5,5), (200,150), (255,255,255), 8)
# Draw a circle, with -1 we can have a colored shape
cv.circle(img, (200,150), 50, (0,255,255), -1)
# True mens close first point to last end
points = np.array([[30,50],[300,200],[100,70],[40,100]], np.int32)
cv.polylines(img, [points], True, (255,0,0), 5 )
"""
# Text on the image
font = cv.FONT_HERSHEY_COMPLEX
# 1 is font size , 2 is thickness
cv.putText(img, 'salam be hame', (20,50), font, 1, (255,255,255), 2, cv.LINE_AA)

cv.imshow('Navid pic', img)
cv.waitKey(0)
cv.destroyAllWindows()
