import cv2

image = cv2.imread("lesson1/cat.png", cv2.IMREAD_COLOR)

b,g,r = cv2.split(image)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
