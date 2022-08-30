import cv2

print(cv2.__version__)
width=640
height=360

snipW = 120
snipH = 60

boxCR = int(height/2)
boxCC = int(width/2)

deltaRow = 1
deltaColumn = 1

cam=cv2.VideoCapture(0)

while True:

    ignore, frame =  cam.read()
    frame = cv2.resize(frame,(width, height))
    ROIframe = frame[boxCR-int(snipH/2):boxCR+int(snipH/2), boxCC-int(snipW/2):boxCC+int(snipH/2)]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[boxCR-int(snipH/2):boxCR+int(snipH/2), boxCC-int(snipW/2):boxCC+int(snipH/2)] = ROIframe

    if boxCR-int(snipH/2) <= 0 or boxCR+int(snipH/2) >= height:
        deltaRow = deltaRow * (-1)

    if boxCC-int(snipW/2) <= 0 or boxCC+int(snipW/2) >= width: 
        deltaColumn = deltaColumn * (-1)

    boxCC=boxCC+deltaColumn
    boxCR=boxCR+deltaRow


    cv2.imshow('MyWin',frame)
    cv2.moveWindow('MyWin',0,0)
    cv2.imshow('ROI Frame',ROIframe)
    cv2.moveWindow('ROI Frame',width,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

