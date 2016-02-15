import numpy as np
import cv2

tree_image = cv2.imread('tree.jpg')
logo_image = cv2.imread('opencv-logo.jpg')

# Transform image to gray scale
bw_logo_image = cv2.cvtColor(logo_image,cv2.COLOR_BGR2GRAY)
# Binarize image with a threshold
ret, mask = cv2.threshold(bw_logo_image,240, 255, cv2.THRESH_BINARY)
# Invert mask
inv_mask = cv2.bitwise_not(mask)

# Extract rows, columns and channels from logo image
rows, cols, channels = logo_image.shape

# Extract roi area in the image with the same size of the mask
image_roi = tree_image[ 50:rows+50, 100:cols+100 ]
# Paint logo area in black given tree image roi
tree_image_black_logo_area = cv2.bitwise_and(image_roi, image_roi, mask = mask)

# Take only logo region from logo image
take_roi_from_logo_image = cv2.bitwise_and(logo_image, logo_image, mask = inv_mask)

# Add roi image with black area for logo with extracted logo image
result = cv2.add(tree_image_black_logo_area, take_roi_from_logo_image)

# Replace image area with result image
tree_image[ 50:rows+50, 100:cols+100 ] = result

cv2.imshow('logo-image', logo_image)
cv2.imshow('gray-logo', bw_logo_image)
cv2.imshow('mask', mask)
cv2.imshow('tree-image-black-logo', tree_image_black_logo_area)
cv2.imshow('take-roi-from-logo-image', take_roi_from_logo_image)
cv2.imshow('result-image', result)
cv2.namedWindow('final-image', cv2.WINDOW_NORMAL)
cv2.imshow('final-image', tree_image)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



