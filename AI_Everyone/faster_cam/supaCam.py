import cv2
import imutils

print(cv2.__version__)
width=1280
height=700
rows=3
columns=4
cam=cv2.VideoCapture(0)

while True:
    ignore, frame =  cam.read()

    #frame = imutils.resize(frame, width, height)
    frame = cv2.resize(frame,(int(width/columns), int(height/columns)))

    for i in range(0, rows):
        for j in range(0, columns):
            window_name = f"Window_{i}x{j}"
            scaled_width = j * int(width/columns)
            scaled_height = i * int(height/columns + 30)           
            cv2.imshow(window_name, frame)
            cv2.moveWindow(window_name, scaled_width, scaled_height)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
