import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object

# For OpenCV 3.0
#fourcc = cv2.VideoWriter_fourcc(*'XVID')         

# For OpenCV 2.4.8, 2.4.9 and possibly 2.4.x
fourcc = cv2.cv.CV_FOURCC(*'XVID')

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # write frame
        out.write(frame)

        # show frame
        cv2.imshow('My video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release objects when finished
cap.release()
out.release()
cv2.destroyAllWindows()





    

