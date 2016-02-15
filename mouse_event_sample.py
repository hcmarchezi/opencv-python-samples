import numpy as np
import cv2

# mouse callback function
def mouseCallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)

# create window
cv2.namedWindow('sample-window')

# connect mouse event for that window to callback function
cv2.setMouseCallback('sample-window',mouseCallback)

while(1):
    # show image
    cv2.imshow('sample-window',img)

    # capture key space or esc
    if cv2.waitKey(20) & 0xFF == 27:
        break

# release windows
cv2.destroyAllWindows()

