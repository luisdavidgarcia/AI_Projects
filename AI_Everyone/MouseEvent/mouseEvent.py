import cv2
import time

evt=0
roi_live = 1

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Left Down: {event}')
        pnt=(xPos,yPos)
        evt=event
    if event == cv2.EVENT_LBUTTONUP:
        print(f'Left Up: {event}')
        pnt=(xPos,yPos)
        evt=event
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'Right: {event}')
        evt=event


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

cv2.namedWindow('myWin')
cv2.setMouseCallback('myWin',mouseClick)

tLast = time.time()
# to ensure no division by zero
time.sleep(.1)

start_point = (0,0)
end_point = (0,0)

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
    cv2.imshow('myWin',frame)

    if evt == 1:
        start_point = pnt

    if evt == 4:
        end_point = pnt

    if evt != 2 and ( start_point != (0,0) and end_point !=  (0,0) ):
        roiFrame = frame[start_point[0]:end_point[0], start_point[1]:end_point[1]]    
        cv2.imshow('ROI', roiFrame)    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

