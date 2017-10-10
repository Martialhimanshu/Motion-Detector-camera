import cv2
f_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("college.jpg")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = f_cascade.detectMultiScale(grey_img,scaleFactor = 1.17, minNeighbors = 5)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
img = cv2.resize(img,(int(img.shape[0]/2),int(img.shape[0]/3)))
cv2.imshow("myface",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
