import cv2

image = cv2.imread("lesson4/coolcat.jpg")

cv2.imshow("Original Image", image)

cv2.waitKey(0)

line1 = cv2.line(image, (50, 60), (80, 90), (245, 252, 38), 10)
line2 = cv2.line(line1, (80,90), (90, 120), (83, 28, 235), 10)
line3 = cv2.line(line2, (90, 120), (100, 180), (141, 196, 112), 10)
cv2.imshow("Image with line", line3)
image = cv2.imread("lesson4/coolcat.jpg")

imagewithtext = cv2.putText(image, "Cool Cat", (50,90), cv2.FONT_HERSHEY_PLAIN, 3.25, (0, 251, 255), 6)
cv2.imshow("CoolCat", imagewithtext)

cv2.waitKey(0)