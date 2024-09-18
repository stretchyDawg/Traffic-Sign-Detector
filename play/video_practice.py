import numpy as np
import cv2

def main():
    capture = cv2.VideoCapture(0)
    
    while True:
        frame_returned, frame = capture.read() # if the frame returned or not, the frame
        width = int(capture.get(3))
        height = int(capture.get(4)) # 4 is the 3rd property of a capture, look up documentation for more properties
        
        image = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=.5, fy=.5)
        image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
        image[:height//2, width//2:] = smaller_frame
        image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
        image[height//2:, width//2:] = smaller_frame
        
        cv2.imshow('Video frame', image)
        
        if(cv2.waitKey(1) == ord('q')):
            break
        
    capture.release()
    cv2.destroyAllWindows()
    
    
    
if __name__ == "__main__":
    main()