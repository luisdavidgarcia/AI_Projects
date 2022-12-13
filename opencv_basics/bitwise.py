import cv2 as cv
import numpy as np

rows = 400
cols = 400

blank = np.zeros((rows, cols), dtype='uint8')

color = 255
start_point = (30,30)
end_point = (370,370)
thickness = -1

rectangle = cv.rectangle(blank.copy(), start_point, end_point, color, thickness)
cv.imshow("Rectangle", rectangle)

circle_center = (200,200)
radius = 200
circle = cv.circle(blank.copy(), circle_center, radius, color, thickness)
cv.imshow("Circle", circle)

# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

#bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

#bitwise NOT --> inverts the image
bitwise_not = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)