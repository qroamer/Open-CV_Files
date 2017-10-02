#https://realpython.com/blog/python/face-recognition-with-python/
import cv2
imagePath = "/home/pi/Pictures/Group2016.jpg"
cascPath = "/home/pi/FaceDetect/haarcascade_frontalface_default.xml"

#This is the cascade
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
	#Changed "flags = cv2.cv.CV_HAAR_SCALE_IMAGE" to:
    flags = cv2.CASCADE_SCALE_IMAGE
)
print("Found {0} Faces".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#cv2.rectangle(image, ellipse, (0, 255, 0), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)
