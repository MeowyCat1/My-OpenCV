import cv2

city = cv2.imread("lesson4/city.png")
# First line
sp = (500,500)
ep = (600,600)
colour = (255, 105, 230)
linethickeness = 50


drawnimage = cv2.line(city, sp, ep, colour, linethickeness)

cv2.imshow("City with line", drawnimage)

cv2.waitKey(0)