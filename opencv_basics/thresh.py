import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

max_pixel_value = 255
block_value = 11
constant_value = 3

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, max_pixel_value, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, max_pixel_value, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded Inverse", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, max_pixel_value, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_value, constant_value)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)