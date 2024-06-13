import cv2 as cv 
import numpy as np     
import matplotlib.pyplot as plt 

image =cv.imread("./img/Star.png")
image_gray =cv.imread("./img/Star.png", 0)


corners = cv.cornerHarris(image_gray, 3, 7, 0.04)

corners_dilated = cv.dilate(corners, None)
image[corners_dilated > 0.01*corners_dilated.max()] = [255,0,0]

plt.imshow(image)
plt.show()