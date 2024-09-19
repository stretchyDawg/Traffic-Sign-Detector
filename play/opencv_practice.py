import cv2
import random
import os

def main(): 
    output_folder = 'play/output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Flags:
    # -1, cv2.IMREAD_COLOR: Default, Loads image in color, Transparency will be neglected
    # 0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale
    # 1, cv2.IMREAD_UNCHANGED: Loads image in color, Transparency will be saved
    img = cv2.imread('assets/STOP_SIGN.png', 1) # 0,0 is in the TOP LEFT
    img = cv2.resize(img, (400, 400))
    cv2.imwrite(os.path.join(output_folder, 'opencv_play_img_original.png'), img)
    
    print(img, end="\n\n")             # read values as 'blue, green, red'
    print(img[20], end="\n\n")         # one row
    print(img[20][10:40], end="\n\n")  # collection of pixels in row
    print(img[20][20], end="\n\n")     # one pixel
    print("Shape:", img.shape)         # (Height, width, channels)
    
    # editing pixels
    for i in range(150):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(200, 255), random.randint(0, 255), random.randint(0, 0)]
    
    # copying and pasting
    tag = img[150:250, 300:400]
    img[1:101, 300:400] = tag
    cv2.imwrite(os.path.join(output_folder, 'opencv_play_img_edited.png'), img)
    
    cv2.imshow('Image',  img)
    cv2.waitKey(0) # 0 is wait infinitely
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()