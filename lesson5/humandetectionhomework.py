import cv2
import numpy as np

people = cv2.imread("lesson2/cat.jpg")

grey = cv2.cvtColor(people, cv2.COLOR_BGR2GRAY)
blurred = cv2.blur(grey, (3,3))

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 1
params.maxThreshold = 9999

detector = cv2.SimpleBlobDetector_create(params)

points = detector.detect(blurred)


markedimage = cv2.drawKeypoints(people, points, np.zeros((1,1)), (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image", markedimage)

cv2.waitKey(0)