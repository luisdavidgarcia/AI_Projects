import cv2
print(cv2.__version__)

def reSizing(frame):
    #define the screen resulation
    screen_res = 660,1040 
    scale_width = screen_res[0] / frame.shape[1]
    scale_height = screen_res[1] / frame.shape[0]
    scale = min(scale_width, scale_height)
    #resized window width and height
    window_width = int(frame.shape[1] * scale)
    window_height = int(frame.shape[0] * scale)

    return (window_width,window_height)

cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    window_params = reSizing(grayFrame)
    window_width = window_params[0]
    window_height = window_params[1]

    window_params2 = reSizing(frame)
    window_width2 = window_params2[0]
    window_height2 = window_params2[1]

    #cv2.WINDOW_NORMAL makes the output window resizealbe
    #Upper Left Window
    cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
    #resize the window according to the screen resolution
    cv2.resizeWindow('Resized Window', window_width, window_height)
    cv2.imshow('Resized Window',grayFrame)
    cv2.moveWindow('Resized Window',0,0)

    #Upper Right Window
    cv2.namedWindow('Resized Window3', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resized Window3', window_width2, window_height2)
    cv2.imshow('Resized Window3',frame)
    cv2.moveWindow('Resized Window3',660,0)

    #Lower Right Window
    cv2.namedWindow('Resized Window2', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resized Window2', window_width, window_height)
    cv2.imshow('Resized Window2',grayFrame)
    cv2.moveWindow('Resized Window2',660,400)

    #Lower Left Window
    cv2.namedWindow('Resized Window4', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Resized Window4', window_width2, window_height2)
    cv2.imshow('Resized Window4',frame)
    cv2.moveWindow('Resized Window4',0,400)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
