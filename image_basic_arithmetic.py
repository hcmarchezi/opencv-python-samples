import numpy as np
import cv2
from matplotlib import pyplot as plt

face_image = cv2.imread('human-face.png')
face_image = face_image[:,0:546]

logo_image = cv2.imread('mars500-small.jpg')

modulo_sum_img = face_image + logo_image
opencv_sum_img = cv2.add(face_image, logo_image)

blended_img = cv2.addWeighted(face_image,0.8,logo_image,0.2,0)


cv2.imshow('face-image', face_image)
cv2.imshow('logo-image', logo_image)
cv2.imshow('modulo-sum-image-image', modulo_sum_img)
cv2.imshow('simple-sumimage', opencv_sum_img)

cv2.imshow('blended-image', blended_img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()