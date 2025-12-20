import cv2
import os
import numpy

haar_file= "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson8/haarcascade_frontalface_default.xml"

# Datasets

path = "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson8/dataset/anything-that-you-want"

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