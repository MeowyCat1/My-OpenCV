import cv2

cat = cv2.imread("lesson3/cat.jpg")

cv2.imshow("Unchanged Image", cat)

cv2.waitKey(0)

# Use cv2.cvtColor() function to convert the image to greyscale
greyscaleimage = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)

cv2.imshow("Greyscale Image", greyscaleimage)
cv2.waitKey()

(row, col) = cat.shape[0:2]

# loop over every pixel in the image

for i in range(row):
    for j in range(col):
        # Using a weighted average to calculate the pixels - clearer grayscale
        B, G, R = cat[i, j]
        gray = 0.114 * B + 0.587 * G + 0.299 * R
        cat[i, j] = gray
        # Find the average of the BGR pixel values - more pixelated
        #img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow("PixelatedCat", cat)

cv2.waitKey(0)