import cv2 as cv
import numpy as np
if __name__ == '__main__':
    img=np.zeros((30,100,3),np.uint8)
    for i in range(100):
        img[15,i]=[0,0,255]
        img[18,i]=[255,0,0]
    cv.imshow('img',img)
    cv.waitKey(0)
    print(cv.__version__)