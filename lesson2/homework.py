import cv2

hill = cv2.imread("lesson2/hill.jpg")
sunset = cv2.resize(cv2.imread("lesson2/sunset.jpg"), (1200,900))

mergedimage = cv2.addWeighted(hill, 0.7, sunset, 0.75, -50)
cv2.imshow("Sunset on the hill", mergedimage)

cat = cv2.imread("lesson2/cat.jpg")
catmask = cv2.imread("lesson2/catmask.jpg")
catnegated = cv2.subtract(cat, catmask)
cv2.imshow("Subtracted Cat", catnegated)

cv2.waitKey(0)