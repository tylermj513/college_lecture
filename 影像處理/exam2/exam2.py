# import numpy as np
# import cv2
# image = cv2.imread("img2.jpg") 
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower_red = np.array([0,50,50]) #example value
# upper_red = np.array([10,255,255]) #example value
# mask = cv2.inRange(hsv, lower_red, upper_red)
# # res = cv2.bitwise_and(image, image, mask=mask)  
# image[np.where((image == [0,0,0]).all(axis = 2))] = [255,100,255]   


# # cv2.imshow('Input', image)
# cv2.imshow('Result', image)
# cv2.waitKey(0) 
import cv2 as cv
import numpy as np

# Load the aerial image and convert to HSV colourspace
image = cv.imread("img2.jpg")
x, y = image.shape[0:2]
image = cv.resize(image, (int(y / 2), int(x / 2)))

image2 = cv.imread("img2.jpg")
x, y = image2.shape[0:2]
image2 = cv.resize(image2, (int(y / 2), int(x / 2)))

hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

hsv2=cv.cvtColor(image2,cv.COLOR_BGR2HSV)
# Define lower and uppper limits of what we call "brown"
lower_red = np.array([0,50,50]) #example value
upper_red = np.array([10,255,255]) #example value

# Mask image to only select browns
mask=cv.inRange(hsv,lower_red,upper_red)

mask2=cv.inRange(hsv2,lower_red,upper_red)
# Change image to red where we found brown
image[mask>0]=(0,255,255)# yellow 
image2[mask2>0]=(255,255,0)# blue

cv.imshow("yellow.png",image)

cv.imshow("blue.png",image2)
cv.waitKey(0) 