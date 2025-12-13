import cv2, time, sys
import numpy as np
print(cv2.__version__)
#record video first
video_path = "C:/Users/samht/OneDrive/Documents/Jetlearn Python/OpenCV/lesson7/video.mp4"

try:
    raw_video = cv2.VideoCapture(video_path)
except:
    print("Video could not be opened")
    sys.exit(1)

time.sleep(1)
background = None
max_background_frames = 120
background_found = False

for i in range(max_background_frames):
    ret, frame = raw_video.read()
    if not ret:
        continue
    background = frame.copy()
    background_found = True
    break
if not background_found:
    print("Could not find any background. Please check the camera or video file.")
    sys.exit(1)

background = np.flip(background, 1)

while raw_video.isOpened():
    ret, img = raw_video.read()
    if not ret:
        print("End of video - could not read frame")
        break
    img = np.flip(img, 1)
    hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red1 = np.array([0,120,70])
    red2 = np.array([10, 120, 70])
    red3 = np.array([20, 120, 70])
    red4 = np.array([30, 120, 70])
    green1 = np.array([100, 0, 0])
    green2 = np.array([180, 100, 100])
    mask = cv2.inRange(hsvimg, green1, green2)

    kernel = np.ones((3,3),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iterations= 2, kernel= kernel)
    mask = cv2.dilate(mask, kernel, iterations= 1)
    maskinv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(img, img, mask=maskinv)
    final_output = cv2.addWeighted(res1,1, res2, 1,0)
    cv2.imshow("Output", final_output)
    if cv2.waitKey(10) & 0xFF == 27:
        break
raw_video.release()
cv2.destroyAllWindows()