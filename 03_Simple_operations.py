import numpy as np 
import cv2 as cv 

img = cv.imread('./img/navidPic.jpg', cv.IMREAD_COLOR)
# Convert color to gray via cv
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


print(img.shape) # (800, 800, 3)
print(img_gray.shape) # (800, 800)
print(img.size) # 1920000
print(img.dtype) # uint8



# seperate different colors in an color image - BGR - (800, 800, 3)
# b = img[:,:, 0]
# g = img[:,:, 1]
# r = img[:,:, 2]

# split an image to channels
b,g,r = cv.split(img)
# merge channels to image
img = cv.merge((b,g,r))

cv.imshow('Navid pic', img)
cv.imshow('BLUE', b)
cv.imshow('GREEN', g)
cv.imshow('RED', r)



# crop the pic
# img2 = img_gray[100:300, 250:500]
head_section = img[150:460, 290:550]
img[0:310, 0:260] = head_section



# work with a spicific area of the pic
# img_gray[100:300, 250:500] = 255
# img[70:300, 50:200] = [25,25,25]


# cv.imshow('Navid pic', img)
# cv.imshow('Navid gray pic', img_gray)
# cv.imshow('Navid pic crop', img2)
# cv.imshow('Navid head', head_section)
cv.waitKey(0)
cv.destroyAllWindows()

