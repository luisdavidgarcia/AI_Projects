import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# image to compare with training data
img = cv.imread(r"Resources/Faces/val/ben_afflek/2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)   

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

green_color = (0, 255, 0)
font = cv.FONT_HERSHEY_COMPLEX
thickness = 2
start_point = (20,20)
font_size = 1.0

# y is the height, x is the width, w is the endpoint of width, h is the endpoint of height
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence of {confidence}")
    cv.putText(img, str(people[label]), start_point, font, font_size, green_color, thickness)
    cv.rectangle(img, (x, y), (x+w, y+h), green_color, thickness)

cv.imshow("Detected Face", img)

cv.waitKey(0)