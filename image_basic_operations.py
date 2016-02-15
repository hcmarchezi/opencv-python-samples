import numpy as np
import cv2

# read and display original image
image = cv2.imread('mars500.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

# extracting ROI
image_roi = image[200:500,250:550]
cv2.namedWindow('ROI', cv2.WINDOW_NORMAL)
cv2.imshow('ROI',image_roi)

# modified image with ROI image
image[10:310,10:310] = image_roi
cv2.namedWindow('Modified', cv2.WINDOW_NORMAL)
cv2.imshow('Modified',image)

# extracting each color channel separately
b, g, r = cv2.split(image)
# merging back to image
image = cv2.merge((b,g,r))

# extract blue channel
blue_pixels = image[:,:,0]
cv2.namedWindow('blue-pixels', cv2.WINDOW_NORMAL)
cv2.imshow('blue-pixels', blue_pixels)

# extract green channel
green_pixels = image[:,:,1]
cv2.namedWindow('green-pixels', cv2.WINDOW_NORMAL)
cv2.imshow('green-pixels', green_pixels)

# extract red channel
red_pixels = image[:,:,2]
cv2.namedWindow('red-pixels', cv2.WINDOW_NORMAL)
cv2.imshow('red-pixels', red_pixels)



cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()