import cv2

image = cv2.imread("lesson1/cat.png", cv2.IMREAD_COLOR)

bwimage = cv2.imread("lesson1/cat.png", cv2.IMREAD_GRAYSCALE)

unchangedimage = cv2.imread("lesson1/cat.png", cv2.IMREAD_UNCHANGED)

bwimagewithnum = cv2.imread("lesson1/cat.png", 0)

cv2.imshow("My Cat Photo", image)
cv2.imshow("My Black and White Cat Photo", bwimage)
cv2.imshow("My Unchanged Cat Photo", unchangedimage)
cv2.imshow("My Numbery Black and White Cat Photo", bwimagewithnum)

cv2.waitKey(0)
cv2.destroyAllWindows()
