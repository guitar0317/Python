import cv2
import numpy as np

try:
    imgR = np.zeros((500,500,3),dtype='uint8')
    imgR[150:350, 150:350] = [0,0,255]

    imgB = np.zeros((500,500,3),dtype=np.uint8)
    imgB[150:350, 150:350] = [255,0,0]

    imgG = np.zeros((500,500,3),dtype=np.uint8)
    imgG[150:350, 150:350] = [0,255,0]
        
    cv2.imshow("imgR",imgR)
    cv2.imshow("imgB",imgB)
    cv2.imshow("imgG",imgG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print("Error")