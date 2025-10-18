import cv2
import os
#Location of the file
file_location = "lesson2"

cat = cv2.imread("lesson2/cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("MEOW!!!!!!", cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Change the execution directory
os.chdir(file_location)
cv2.imwrite("catblackandwhite.jpg", cat)