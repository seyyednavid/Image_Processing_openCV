import numpy as np     
import cv2 as cv 
import matplotlib.pyplot as plt 

# for finding similar objects
image = cv.imread("./img/building1.jpg", 0)
template = cv.imread("./img/building1_temp.jpg", 0)

w,h = template.shape

result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

threshold = 0.6
locations = np.where(result >= threshold)
for point in zip(*locations[::-1]):
    cv.rectangle(image, point, (point[0] + h, point[1] + w), (255,255,0), 2)

plt.imshow(image)
plt.show()
