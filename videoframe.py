"""Author: Martial Himanshu
licence: General public licences
Interpreter: Python 3.6.2
features: 1. Can detect any type of motion around the environment
          2. can detect human as well as animals motion
          3. Generates csv file of list of time parameter when motion appears and vanished
          4. Also generates chart for motion detection
          5. Easy to use for night vision camera to capture motion in dark 
version: 2017.1 and next is coming soon"""

import cv2,time,pandas
from datetime import datetime
#f_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
first_frame = None
"store first image as list of numpy array's data"
video = cv2.VideoCapture(0)
status_list=[None,None]
times=[]
df = pandas.DataFrame(columns=["Start","End"])

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    "Applying GaussianBlur to image to reduce noise and other disturbance from video"
    # faces = f_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=7)
    # for x,y,w,h in faces:
    #      gray = cv2.rectangle(frame,(x,y),(x+w,y+h),(125,200,99),2)
    # # cv2.imshow("capturing",frame)
    if first_frame is None:
        "Checking for first image in memory"
        first_frame = gray
        continue

    deltaFrame = cv2.absdiff(first_frame,gray)
    threshFrame =cv2.threshold(deltaFrame,50,255,cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame,None,iterations= 2)

    (_,cnts,_) = cv2.findContours(threshFrame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue
        status = 1
        "Status will change if any object movement captured in camera has area greater tthan 10000"
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())

    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("gray",gray)
    cv2.imshow("Delta Frame",deltaFrame)
    cv2.imshow("Threshold Frame", threshFrame)
    cv2.imshow("Color Frame",frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)
"Prints data of status list and time data of motion detection in terminal"

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("detect.csv")
video.release()
cv2.destroyAllWindows()
