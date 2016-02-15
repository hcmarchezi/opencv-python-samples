import numpy as np
import cv2

image = cv2.imread('tree.jpg')

# Acessing RGB color at pixel 310,190
pixel = image[10,10]
print ("color at pixel(310,190) = " + str(pixel))

# Acesssing blue component in RGB color in pixel 310,190
blue = image[10,10,0]
print ("blue component at pixel (310,190) = " + str(blue))

# Acesssing green component in RGB color in pixel 310,190
green = image[10,10,1]
print ("green component at pixel (310,190) = " + str(green))

# Acesssing red component in RGB color in pixel 310,190
red = image[10,10,2]
print ("red component at pixel (310,190) = " + str(red))

# Image properties
print ("image rows, columns and channels: " + str(image.shape))
print ("image size: " + str(image.size))
print ("data type: " + str(image.dtype))











