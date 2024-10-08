import numpy as np
import cv2

def main():
    img = cv2.imread('assets/soccer_practice.png', 0)
    img = cv2.resize(img, (0,0), fx=.8, fy=.8)
    template = cv2.imread('assets/soccer_shoe.png', 0)
    template = cv2.resize(template, (0,0), fx=.8, fy=.8)

    h, w = template.shape
    
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    
    for method in methods:
        img2 = img.copy()
        
        # (W - w + 1, H - h + 1)
        # Say: W = 4, w = 2, H = 4, h = 2
        # 4-2+1 = 3, 4-2+1 = 3
        # 
        # 
        # [
        #  [255, 255, 255, 255]
        #  [255, 255, 255, 255]
        #  [255, 255, 255, 255]
        #  [255, 255, 255, 255]
        # ]
        #        
        # [
        #  [255, 255]
        #  [255, 255]
        # ]
        # 
        # [
        #  [0, 0, 0]
        #  [0, 1, 0]
        #  [0, 0, 0]
        # ]
        
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(min_loc, max_loc)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc
        
        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(img2, location,bottom_right, 255, 5)
        cv2.imshow('Match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()