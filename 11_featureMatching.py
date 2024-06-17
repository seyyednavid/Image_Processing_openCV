import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv.imread("./img/desert.webp")

# 1 - SIFT
# feat_sift = cv.SIFT_create()
# sift_keypoints, descriptors1 = feat_sift.detectAndCompute(image, None)
# image_sift = cv.drawKeypoints(image, sift_keypoints, None)


# 2 - SURF works on opencv version 3.4
# surf = cv.SURF_create()
# surf_keypoints, descriptors2 = surf.detectAndCompute(image, None)
# image_surf = cv.drawKeypoints(image, surf_keypoints, None)


# ORB
# feat_orb = cv.ORB_create(nfeatures=1000)
# orb_keypoints, descriptors3 = feat_orb.detectAndCompute(image, None)
# image_orb = cv.drawKeypoints(image, orb_keypoints, None)

# Display the result
# plt.imshow(image_orb)
# plt.show()


# feature matching with orb's features
image1 = cv.imread("./img/book1.png")
image2 = cv.imread("./img/book2.png")

feat_orb = cv.ORB_create(nfeatures=1000)

orb_keypoints1, descriptors1 = feat_orb.detectAndCompute(image1, None)
orb_keypoints2, descriptors2 = feat_orb.detectAndCompute(image2, None)

#Determine feature matching between two images
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

matches = sorted(matches, key=lambda x:x.distance)
image_matches = cv.drawMatches(image1, orb_keypoints1, image2, orb_keypoints2, matches[:100], None, flags=2)

plt.imshow(image_matches)
plt.show()