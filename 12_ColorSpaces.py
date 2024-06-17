import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt  

image_bgr = cv.imread("./img/blue_eyes.jpg")
img_gray =cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)

# convert BGR to RGB
image_rgb = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)

# RGB => matplotlib
# BGR  => opencv
# BGRA or RGBA => 4 channels - alpha opacity
# HSV  Hue Saturation Value [20,100,100]
image_hsv = cv.cvtColor(image_bgr, cv.COLOR_BGR2HSV)

# blue_ch, green_ch, red_ch = cv.split(image)

"""
cv.imshow('IMAGE DISPLAY',image)
cv.imshow('BLUE DISPLAY',blue_ch)
cv.imshow('GREEN DISPLAY',green_ch)
cv.imshow('RED DISPLAY',red_ch)
cv.waitKey(0)
cv.destroyAllWindows()
"""

plt.imshow(image_hsv)
plt.show()