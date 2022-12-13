import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #works on images, videos, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #works on live video only
    capture.set(3,width)
    capture.set(4, height)

capture = cv.VideoCapture(0)

while(True): #while loop is needed since a video is just multiple images in a loop
    isTrue, frame = capture.read() #returns two values a boolean and a frame
    changeRes(200, 300)
    cv.imshow("Video", frame) #attains each frame to display it as a video

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

#img = cv.imread('Resources/Photos/cat.jpg')
#cv.imshow('Cat', img)

#resized_image = rescaleFrame(img)
#cv.imshow('Image', resized_image)

cv.waitKey(0)

