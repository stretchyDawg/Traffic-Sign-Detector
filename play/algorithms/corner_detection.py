import numpy as np
import cv2

N = 100

def main():
    img = cv2.imread('assets/chessboard.png')
    img = cv2.resize(img, (0,0), fx=.75, fy=.75)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #                                (number of corners, minimum quality, minimum euclidean distance)
    corners = cv2.goodFeaturesToTrack(gray, N, .0000001, 10)
    corners = np.int64(corners)
    for corner in corners:
        x, y = corner.ravel()
        print(x, ", ", y, sep = "")
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
    
    cv2.imshow('Frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()








if __name__ == "__main__":
    main()