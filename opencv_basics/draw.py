import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# Colors (bgr)
blue = 255,0,0
green = 0,255,0
red = 0,0,255

# Image pixel parameters 
height_start = 0
height_end = 250
width_start = 0
width_end = 250

# draw a square
#blank[height_start:height_end, width_start:width_end] = blue
#cv.imshow("Green", blank)

# draw a rectangle
#cv.rectangle(blank, (width_start, height_start), (width_end, height_end), (green), thickness=-1)
#cv.imshow("Rectangle", blank)

# draw a circle
#radius = 40
#cv.circle(blank, (width_end, height_end), radius, (red), thickness=-1)
#cv.imshow("Circle", blank)

# draw a line
#cv.line(blank, (width_start, height_start), (width_end, height_end), (blue), thickness=3)
#cv.imshow("Line", blank)

# write text
font = cv.FONT_HERSHEY_TRIPLEX
font_scale = 1.0
cv.putText(blank, "Howdy Bitch", (width_start+50, width_end), font, font_scale, (green), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)

