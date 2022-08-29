import cv2
import imutils

print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0)

while True:
    ignore, frame =  cam.read()

    frame = imutils.resize(frame, width, height)
    cv2.imshow('myCam', frame)
    cv2.moveWindow('myCam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
