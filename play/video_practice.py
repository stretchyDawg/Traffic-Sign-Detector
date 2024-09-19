import numpy as np
import cv2

def main():
    capture = cv2.VideoCapture(0)
    
    while True:
        frame_returned, frame = capture.read() # if the frame returned or not, the frame
        width = int(capture.get(3))
        height = int(capture.get(4)) # 4 is the 3rd property of a capture, look up documentation for more properties
        
        # Hue Saturation Value
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # BGR to HSV
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        cv2.imshow('Video Frame', result)
        cv2.imshow('mask', mask)
        
        if(cv2.waitKey(1) == ord('q')):
            break
        
    capture.release()
    cv2.destroyAllWindows()
    
    
    
if __name__ == "__main__":
    main()