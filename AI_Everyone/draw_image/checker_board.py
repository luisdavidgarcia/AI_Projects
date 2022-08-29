import cv2
import numpy as np

# entire pixel width of image
boardSize = 1000
# number of squares in image
number_of_squares = 8 
# pixel width of each square
square_size = int(boardSize / number_of_squares)


dark_color = (0,0,0)
light_color = (0,0,255)
current_color = dark_color

while True:
    x = np.zeros([boardSize, boardSize, 3], dtype=np.uint8)

    for row in range(0, number_of_squares):
        for column in range(0, number_of_squares):
            #set color
            x[square_size*row:square_size*(row+1), square_size*column:square_size*(column+1)] = current_color
            if current_color == light_color:
                current_color = dark_color
            else:
                current_color = light_color

        if current_color == light_color:
            current_color = dark_color
        else:
            current_color = light_color



    cv2.imshow('Checker Board',x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


