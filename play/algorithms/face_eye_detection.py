import numpy as np
import cv2

def main():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        frame_returned, frame = capture.read() # if the frame returned or not, the frame
        
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #                                    (base image, scale factor (if 1.05, then shrink screen by 5%, the higher the faster but less accurate), minNeighbors (essentially accuracy)
        faces = face_cascade.detectMultiScale(grayscale, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
            
            # getting the pixels from the face to get the eyes faster
            roi_grayscale = grayscale[y:y+w, x:x+w] # roi = region of interest
            roi_color = frame[y:y+w, x:x+h]
            
            eyes = eye_cascade.detectMultiScale(roi_grayscale, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            
        cv2.imshow('Video Frame', frame)
        
        if(cv2.waitKey(1) == ord('q')):
            break
        
    capture.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()