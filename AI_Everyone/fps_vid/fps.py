import cv2
import time

print(cv2.__version__)
width=640
height=360
rows=3
columns=4
upper_left=(400,10)
lower_right=(630,40)
myText = 'fps'
myFont = cv2.FONT_HERSHEY_DUPLEX
fpsFilter = 30

cam=cv2.VideoCapture(0)
tLast = time.time()
# to ensure no division by zero
time.sleep(.1)

while True:
    dT = time.time() - tLast
    fps = int(1/dT)
    fpsFilter = int(fpsFilter*.9+fps*.1)
    tLast = time.time()

    ignore, frame =  cam.read()

    frame = cv2.resize(frame,(width, height))

    myText = f'{fpsFilter} fps' 

    cv2.rectangle(frame,upper_left, lower_right,(0,255,0),-1)
    cv2.putText(frame, myText,(410,35), myFont, 1, (0,0,0),1)
    cv2.imshow('MyWin',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

