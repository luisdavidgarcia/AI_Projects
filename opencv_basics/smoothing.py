import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

kernal_size = (7,7)

# Averaging
average = cv.blur(img, kernal_size)
cv.imshow("Average Blur", average)

# Gaussian Blur
threshold = 0
gauss = cv.GaussianBlur(img, kernal_size, threshold)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
single_kernal = 7
median = cv.medianBlur(img, single_kernal)

# Bilateral
d = 10
sigmaColor = 75
sigmaSpace = 75
bilateral = cv.bilateralFilter(img, d, sigmaColor, sigmaSpace)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)