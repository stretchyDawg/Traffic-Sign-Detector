import numpy as np
import cv2

def main():
    capture = cv2.VideoCapture(0)
    
    while True:
        frame_returned, frame = capture.read() # if the frame returned or not, the frame
        width = int(capture.get(3))
        height = int(capture.get(4)) # 4 is the 3rd property of a capture, look up documentation for more properties
        
        #               (starting pos, ending pos, color, line thickness)
        image = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)
        image = cv2.line(frame, (width,0), (0, height), (0, 0, 255), 10)
        #                    (top left corner, bottom right corner, color, thickness)
        image = cv2.rectangle(image, (100, 100), (200, 200), (128,128,128), 5)
        #                 (center, radius, color, thickness)
        image = cv2.circle(image, (300, 300), 100, (0,255,0), -1)
        
        image = cv2.putText(image, "I have to fart.", (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5, cv2.LINE_AA)
        
        cv2.imshow('Video Frame', image)
        
        if(cv2.waitKey(1) == ord('q')):
            break
        
    capture.release()
    cv2.destroyAllWindows()
    
    
    
if __name__ == "__main__":
    main()