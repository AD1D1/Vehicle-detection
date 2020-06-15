import cv2

camera = cv2.VideoCapture(r"video.avi")
camera.open(r"video.avi")
car_cascade = cv2.CascadeClassifier(r"cars.xml")
while True:
    (grabbed, frame) = camera.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("video.avi", frame)
    if cv2.waitKey(1) == ord('q'):
        sys.exit(0)
camera.release()
cv2.destroyAllWindows()
