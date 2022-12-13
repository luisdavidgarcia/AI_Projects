import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

# mask must be same size of image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Image", blank)

color = 255
center = (img.shape[1]//2, img.shape[0]//2)
thickness = -1
radius = 100

# making weird shapes
start_point = (30,30)
end_point = (370,370)
center = (img.shape[1]//2 + 45, img.shape[0]//2)
circle = cv.circle(blank.copy(), center, radius, color, thickness)
rectangle = cv.rectangle(blank.copy(), start_point, end_point, color, thickness)
werid_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", werid_shape)

mask = cv.circle(blank, center, radius, color, thickness)
cv.imshow("Mask", mask)

start_point = (img.shape[1]//2 - 100, img.shape[0]//2 - 100)
end_point = (img.shape[1]//2 + 100, img.shape[0]//2 + 100)
mask2 = cv.rectangle(blank, start_point, end_point, color, thickness)

# change "mask" to "werid_shape" to see the difference
masked = cv.bitwise_and(img, img, mask=mask2)
cv.imshow("Masked Image", masked)


cv.waitKey(0)