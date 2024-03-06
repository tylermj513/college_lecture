import cv2 as cv
import numpy as np
 
image = cv.imread("img1.jpg")
x, y = image.shape[0:2]
image = cv.resize(image, (int(y/ 3), int(x / 3)))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(gray, (11, 11), 0)

canny = cv.Canny(blurred, 30, 45) 
 
cnts, _ = cv.findContours(canny.copy(), cv.RETR_EXTERNAL,
cv.CHAIN_APPROX_SIMPLE)
 

contours = image.copy()
cv.drawContours(contours, cnts, -1, (0, 255, 0), 2)
cv.putText(contours, "Detect there are {} boats on the sea ". format(len(cnts)-26), (10, 40), cv.FONT_HERSHEY_SIMPLEX,
  1, (255, 0, 0), 1, cv.LINE_AA)
  
print(" 偵測到有{}艘船在海上 ". format(len(cnts)-26))
cv.imshow("Result:", contours)
cv.waitKey(0)

  