import numpy as np
import cv2

# Create a black image for background
img = np.zeros((512,512,3), np.uint8)

# Draw line from (0,0) to (511,255) with color green (0,255,0) and thickness 5
cv2.line(img, (0,0), (511,255), (0,255,0), 5)

cv2.rectangle(img,(384,0),(510,128),(0,0,255),3)

cv2.circle(img,(447,63), 63, (255,0,0), -1)

# check documentation for signature details
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

points = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
points = points.reshape((-1,1,2))
cv2.polylines(img,[points],True,(0,255,255))

# Put text 'My sample text' in position (10,500) with HERSHEY font at size 5 with white color (255,255,255) adn thickness 3
cv2.putText(img, 'My sample text', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 3)

# Show resulting image
cv2.imshow('shapes', img)

# Save resulting image
cv2.imwrite('drawing-output.png',img)

# Wait for key before quit
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


