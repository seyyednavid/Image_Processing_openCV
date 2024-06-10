import numpy as np 
import cv2 as cv 

img1 = cv.imread('navidPic.jpg')
img2 = cv.imread('save1_g_.jpg')

# added = img1 + img2
# added = cv.add(img1, img2)
# added = cv.addWeighted(img1, 0.8, img2, 0.2 , 0)

img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret , mask_img = cv.threshold(img2_gray, 80, 255, cv.THRESH_BINARY) # binary

# if we want replace white to black and vice verca
# mask_inv = cv.bitwise_not(mask_img)

img1_m = cv.bitwise_and(img1, img1, mask = mask_img)

cv.imshow('image 1', img1)
cv.imshow('Mask', img1_m)
# cv.imshow('Added', added)




cv.waitKey(0)
cv.destroyAllWindows()
