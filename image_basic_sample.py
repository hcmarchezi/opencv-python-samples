import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('human-face.png',0)

cv2.namedWindow('Human Face', cv2.WINDOW_NORMAL)
cv2.imshow('Human Face',img)
# cv2.imwrite('new-human-face.png',img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


