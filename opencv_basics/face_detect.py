import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# have to tweak the parameters to get the best results
faces_rect  = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f"Number of faces found = {len(faces_rect)}")

green = (0,255,0)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), green, thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)