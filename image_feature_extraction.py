import numpy as np
import cv2

#image = cv2.imread('human-face.png')
image = cv2.imread('tree.jpg')

image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ORB feature extractor
detector = cv2.ORB(nfeatures = 5000) # Here it could be SIFT, MSER or other image descriptors

# extract keypoint
keypoints = detector.detect(image_bw)

# compute descriptors
keypoints, descriptors = detector.compute(image, keypoints)

print ("keypoints:   " + str(len(keypoints)))
print ("descriptors: " + str(len(descriptors)))

image_with_keypoints = cv2.drawKeypoints(image,keypoints,color=(0,255,255), flags=0)

cv2.namedWindow('image-with-keypoints', cv2.WINDOW_NORMAL)
cv2.imshow('image-with-keypoints', image_with_keypoints)

# Wait for key before quit
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
