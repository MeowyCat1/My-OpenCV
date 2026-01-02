import cv2

car_cascade = cv2.CascadeClassifier("lesson10/cars.xml")

video = cv2.VideoCapture("/Users/samfussey/Library/CloudStorage/OneDrive-Personal/Documents/Jetlearn Python/OpenCV/lesson10/cars.mp4")

while True:
    ret, img = video.read()
    if not ret:
        break
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grey)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow("Car Feed", img)
    if cv2.waitKey(10) == 27:
        break
video.release()
cv2.destroyAllWindows()