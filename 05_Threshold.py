import numpy as np
import cv2 as cv 

# img_book = cv.imread('bookpage.jpg')
img_book = cv.imread('./img/brainmri.jpeg')
img_book_gray = cv.cvtColor(img_book, cv.COLOR_BGR2GRAY)
ret, thresh1= cv.threshold(img_book_gray, 132, 255, cv.THRESH_BINARY)

# OTSU Thresholding => automatically determine proper threshold number
ret2, thresh2 = cv.threshold(img_book_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print(ret2) # 22

# Adaptive Thresholding=> threshold for each region of pic
thresh3 = cv.adaptiveThreshold(img_book_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 15, 1 )


cv.imshow('original book page', img_book)
cv.imshow('Threshold', thresh1)
cv.imshow('Threshold + OTSU', thresh2)
cv.imshow('Threshold + adaptiveThreshold', thresh3)


cv.waitKey(0)
cv.destroyAllWindows()
