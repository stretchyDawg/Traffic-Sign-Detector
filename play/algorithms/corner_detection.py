import numpy as np
import random
import cv2

N = 500
FILENAME = 'assets/chessboard.png'

def main():
    img = cv2.imread(FILENAME)
    img = cv2.resize(img, (0,0), fx=.75, fy=.75)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #                                (number of corners, minimum quality, minimum euclidean distance)
    corners = cv2.goodFeaturesToTrack(gray, N, .5, 10)
    corners = np.int64(corners)
    for corner in corners:
        x, y = corner.ravel()
        print(x, ", ", y, sep = "")
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])
            corner2 = tuple(corners[j][0])
            color = [int(x) for x in np.random.randint(0, 255, size=3)]
            cv2.line(img, corner1, corner2, color, 1)
                
    
    cv2.imshow('Frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()








if __name__ == "__main__":
    main()