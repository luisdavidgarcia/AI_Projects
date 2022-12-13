import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow("Boston", img)

# Translation
def translate(img, x, y):
    width = img.shape[1]
    height = img.shape[0]
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (width, height)
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left shift
# -y --> up shift
# +y --> down shift
# +x --> right shift

translated = translate(img,-100,100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# all rotations are counterclock wise unless angle is negative
# don't do a rotation of a rotated image just add angle and rotate og image
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# flipping
# 0 --> vertical flip
# 1 --> horizontal flip
# -1 --> horizontal and vertical flip
flip = cv.flip(img,0)
cv.imshow("Flipped", flip)

cv.waitKey(0)
