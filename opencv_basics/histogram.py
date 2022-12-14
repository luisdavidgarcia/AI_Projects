import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

center = (img.shape[1]//2, img.shape[0]//2)
radius = 100
color = 255
thickness = -1

mask = cv.circle(blank,center,radius,color,thickness) 

# change to gray to see the difference
image_to_mask = img
masked = cv.bitwise_and(image_to_mask, image_to_mask, mask=mask)
cv.imshow("Mask", masked)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
colors = ('b', 'g', 'r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)