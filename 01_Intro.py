import numpy as np
import cv2 as cv 
from  matplotlib import pyplot as plt

img_gray = cv.imread('./img/navidPic.jpg',cv.IMREAD_GRAYSCALE)
img_color = cv.imread('./img/navidPic.jpg',cv.IMREAD_COLOR)

# cv.IMREAD_GRAYSCALE == 0 = gray color
# cv.INREAD_COLOR == 1  => for having image with colors
# cv.IMREAD_UNCHANGED == -1 => get the pic with original color + alpha

# show and save img without matplotlib
# cv.imshow('IMAGE GRAY DISPLAY', img_gray)
cv.imshow('IMAGE COLOR DISPLAY', img_color)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('save1_g_.jpg', img_gray)


# plt.imshow(img_gray, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(img_color, interpolation = 'bicubic')
# for removing rulers on pics
plt.xticks([]), plt.yticks([])
# create a line on 
plt.plot([50,100],[100,200], 'c', linewidth = 5)
plt.show()

# RGB
# openCV => BGR
# RGBA, BGRA