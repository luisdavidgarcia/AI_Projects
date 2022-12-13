import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)


cv.waitKey(0)