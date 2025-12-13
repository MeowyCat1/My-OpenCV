import cv2
import sys
import numpy
import os

haar_file= "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson8/haarcascade_frontalface_default.xml"

# Datasets

path = "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson8/dataset/anything-that-you-want"

print(path)

(width, height) = (300,300)

face_cascade = cv2.CascadeClassifier(haar_file)

if face_cascade.empty():
    print("HAAR cascade empty")
    sys.exit()

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Webcam is not working")
    sys.exit()

print("Press esc to exit")

# Image Counter

count = 1

while count <=30:
    ret,im = webcam.read()
    if not ret:
        continue
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.1, 3)
    print(f"Faces detected: {len(faces)}")
    # Loop through detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x,y),(x+ w, y+h),(255,0,0),2)
        face = grey[y:y+h, x:x+w] # Extracts only the face from the image
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite(img=face_resize, filename=os.path.join(path,f"{count}.png"))
        count += 1
    cv2.imshow("FaceRecognition", im) # show live webcam feed with rectangle over face
    if cv2.waitKey(10) == 27:
        break

# Release webcam
webcam.release()
#Close OpenCV windows
cv2.destroyAllWindows()