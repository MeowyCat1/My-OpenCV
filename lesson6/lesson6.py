import cv2, os
from PIL import Image
os.chdir("C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson6/images")
path = "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson6/images"

def video():
    videoname = "myvideo.avi"
    images = []
    for img in os.listdir("."):
        if img.lower().endswith((".jpg",".png",".png")):
            images.append(img)
    frame = cv2.imread(os.path.join(".", images[0]))
    height, width, layers = frame.shape()
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video = cv2.VideoWriter(videoname, fourcc, 1, (width,height))
    for image in images:video.write(cv2.imread(os.path.join(".", image)))
    cv2.destroyAllWindows()
    video.release()
    print(f"Video created successfully: {videoname}")

meanwidth, meanheight = 0,0

imagefiles = [f for f in os.listdir('.') if f.lower().endswith(('.jpg','.png','.jpeg'))]
num_of_images = len(imagefiles)

for file in imagefiles:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    meanwidth = meanwidth + width
    meanheight = meanheight + height

meanwidth = meanwidth / num_of_images
meanheight = meanheight / num_of_images

print(f"meanwidth: {meanwidth}, meanheight: {meanheight}")

for file in imagefiles:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    print(f"width: {width}, height: {height}")
    imgResize = img.resize((meanwidth,meanheight), Image.LANCZOS)
    imgResize.save(file, "jpg", quality = 95)
    print(f"filename: {img.filename} resized")

video()