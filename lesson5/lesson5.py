import cv2
import numpy as np
import random as rand

wheel = cv2.imread("lesson5/wheel.jpg")

greyscalewheel = cv2.cvtColor(wheel, cv2.COLOR_BGR2GRAY)

blurredgreyscalewheel = cv2.blur(greyscalewheel, (3,3))


# Param 1 - edge detection threshold
# Param 2 - Number of points needed to classify a circle
detectedcircles = cv2.HoughCircles(blurredgreyscalewheel, cv2.HOUGH_GRADIENT, 1, 15, param1= 50, param2= 55, minRadius= 40, maxRadius= 300)

if detectedcircles is not None:
    detectedcircles = np.uint16(np.around(detectedcircles))

for p in detectedcircles[0,:]:
    a,b,r = p[0],p[1],p[2]
    cv2.circle(wheel, (a,b),r, (rand.randint(0,255),rand.randint(0,255), rand.randint(0,255)), 5)

cv2.imshow("Detected Cirles", wheel)



cv2.waitKey(0)