import cv2,time
f_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:

    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=7)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(125,200,99),2)
    cv2.imshow("capturing",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


time.sleep(1)
video.release()
cv2.destroyAllWindows()
