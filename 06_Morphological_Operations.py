import numpy as np    
import cv2 as cv 
import matplotlib.pyplot as plt 

original_img = cv.imread('./img/cells_threshold.png', 0)
ret, mask = cv.threshold(original_img, 25, 255, cv.THRESH_BINARY)

# using Morphological to remove noise in image



# Erosion
''' Erodes away the boundaries of the foreground object.'''
kernel = np.ones((3,3), np.uint8)
# eroded_img1 = cv.erode(mask, kernel, iterations=1)
kerne2 = np.ones((5,5), np.uint8)
# eroded_img2 = cv.erode(mask, kernel, iterations=1)



# Dilation
''' Increases the white region in the image or the size of the foreground object.'''
# dilated_img = cv.dilate(mask, kernel, iterations=1)



# Closing => 
''' Closing is a dilation followed by an erosion. It is used to close small holes and gaps in the image, 
particularly useful for filling small black regions in an otherwise white area. '''
# closed_img1 = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel )
# closed_img2 = cv.morphologyEx(mask, cv.MORPH_CLOSE, kerne2 )



# opening
'''Opening is an erosion followed by a dilation. It is useful for removing small objects from an image while 
preserving the shape and size of larger objects in the image.'''
# opened_img1 = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
# opened_img2 = cv.morphologyEx(mask, cv.MORPH_OPEN, kerne2)




# Gradient
''' the gradient refers to the difference between the dilation and erosion of an image. 
It is used to highlight the edges of objects within an image'''
gradient1 = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
gradient2 = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kerne2)


fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 20))
cmap_val = 'gray'
ax1.axis("off")
ax1.title.set_text('mask')
ax2.axis("off")
ax2.title.set_text('gradient1')
ax3.axis("off")
ax3.title.set_text('gradient2')
ax1.imshow(mask, cmap=cmap_val)
ax2.imshow(gradient1, cmap=cmap_val)
ax3.imshow(gradient2, cmap=cmap_val)
plt.show()

