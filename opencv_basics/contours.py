import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# 1st Method to Replicate Contours ----------------------------------------
# blur to reduce number of contours and canny to get edges
kernalsize = (5,5)
blur = cv.GaussianBlur(gray,kernalsize,cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

threshold1 = 125
threshold2 = 175
canny = cv.Canny(blur, threshold1, threshold2)
cv.imshow("Canny", canny)

# 2nd Method Using Thresholds of Byte Pixel Values -------------------------
lower_byte_bound = 125 #anything lower than this becomes 0, so black
upper_byte_bound = 255 #anything higher than this becomes 255 (1), so white
ret, thresh = cv.threshold(gray,lower_byte_bound, upper_byte_bound, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contour_method = canny #only change this one to see difference in methods

contours, hierarchies = cv.findContours(contour_method, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!")

contour_index = -1 # -1 means all of them
red_color = (0,0,255)
thickness = 1
cv.drawContours(blank, contours, contour_index, red_color,thickness)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)
