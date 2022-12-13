import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Boston", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur images
odd_kernal1 = 7
odd_kernal2 = 7
kernalsize = (odd_kernal1, odd_kernal2)
blur = cv.GaussianBlur(img, kernalsize, cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# edge cascade
threshold1 = 125
threshold2 = 175
# for max edges pass img, but for less pass a blur
canny = cv.Canny(blur, threshold1, threshold2)
cv.imshow("Canny Edges", canny)

# dilating images
dilated = cv.dilate(canny,kernalsize,iterations=3)
cv.imshow("Dilation", dilated)

# eroding
eroded = cv.erode(dilated,kernalsize,iterations=1)
cv.imshow("Eroded", eroded)

# resize
new_width = 500
new_height = 500
new_dimensions = (new_height, new_width)

resized = cv.resize(img, new_dimensions, interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resized)

# cropping
start_width = 200
end_width = 400
start_height = 50
end_height = 200

cropped = img[start_height:end_height, start_width:end_width]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
