import cv2

#addition
ruins = cv2.imread("lesson2/ruins.jpg")
galaxy = cv2.imread("lesson2/galaxy.jpg")

# provide image1, weight1, image2, weight2, brightness
newimage = cv2.addWeighted(ruins, 0.6, galaxy, 0.4, 0)

#subtraction
star = cv2.imread("lesson2/Star.jpg")
negstar = cv2.imread("lesson2/negstar.jpg")

subtractedimage = cv2.subtract(star, negstar)

#resizing
cat = cv2.imread("lesson2/cat.jpg")
kitten = cv2.resize(cat, (500, 200))

#show images
cv2.imshow("Added image", newimage)
cv2.imshow("Subtracted image", subtractedimage)
cv2.imshow("mew", kitten)

cv2.waitKey(0)