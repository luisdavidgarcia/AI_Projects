import cv2 as cv

#Reading Images
#img = cv.imread("Resources/Photos/cat.jpg")

#cv.imshow("Cat", img)

#Reading Videos
capture = cv.VideoCapture("Resources/Videos/dog.mp4")

while(True): #while loop is needed since a video is just multiple images in a loop
    isTrue, frame = capture.read() #returns two values a boolean and a frame
    cv.imshow("Video", frame) #attains each frame to display it as a video

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.waitKey(0)   #permits user to enter any key to quit 