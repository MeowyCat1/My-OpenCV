import cv2
import os
import numpy
import sys

haar_file= "/Users/samfussey/Library/CloudStorage/OneDrive-Personal/Documents/Jetlearn Python/OpenCV/lesson8/haarcascade_frontalface_default.xml"

# Datasets

path = "/Users/samfussey/Library/CloudStorage/OneDrive-Personal/Documents/Jetlearn Python/OpenCV/lesson8/dataset/anything-that-you-want"

images = []
labels = []
id = 0
names = {}

for (subdirectories, directories, files) in os.walk(path):
    for directory in directories:
        names[id] = directory
        path2 = os.path.join(path, directory)
        for file in os.listdir(path2):
            path3 = os.path.join(path2, file)
            print(path3)
            image =  cv2.imread(path3, 0)
            if image is None:
                continue
            images.append(image)
            labels.append(id)
        id += 1
(images, labels) = [numpy.array(lst) for lst in [images, labels]]

# Training the model YAY!!!!

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)
print("Model trained!")



# Datasets



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

print(names)

while True:
    ret,im = webcam.read()
    if not ret:
        continue
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.1, 3)
    # Loop through detected faces
    for (x, y, w, h) in faces:
        face = grey[y:y+h, x:x+w] # Extracts only the face from the image
        face_resize = cv2.resize(face, (width, height))
        output, accuracy = model.predict(face_resize)
        if accuracy < 65:
            cv2.rectangle(im, (x,y),(x+ w, y+h),(255,0,0),2)
            cv2.putText(im, str(names[output]), (x,y-20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale= 3, color=(255,255,255))
    cv2.imshow("FaceRecognition", im) # show live webcam feed with rectangle over face
    if cv2.waitKey(10) == 27:
        break

# Release webcam
webcam.release()
#Close OpenCV windows
cv2.destroyAllWindows()