import cv2

def main(): 
    img = cv2.imread('assets/STOP_SIGN.png')
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) 
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Flags:
    # -1, cv2.IMREAD_COLOR: Default, Loads image in color, Transparency will be neglected
    # 0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale
    # 1, cv2.IMREAD_UNCHANGED: Loads image in color, Transparency will be saved

    cv2.imshow('Image',  img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()