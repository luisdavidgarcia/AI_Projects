import cv2 as cv
import numpy as np

# Load an image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# blank channels become black, but others become their color
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
# merge all channels, can't really do this for blue, green, and red
merged = cv.merge([b,g,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
cv.imshow("Merged", merged)

# bgr images have 3 shapes
print(img.shape)
# gray scale images only have one shape
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)