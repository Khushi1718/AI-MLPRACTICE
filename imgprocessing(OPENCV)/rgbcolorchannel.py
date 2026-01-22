import cv2
import numpy as np
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")
# img[:,:,0]=0 # set blue channel to 0
# img[:,:,1]=0    # set green channel to 0  
# img[;,;,2]=0    # set red channel to 0

imgBlue=img[:,:,0]
imgGreen=img[:,:,1]
imgRed=img[:,:,2]

new_img = np.hstack((imgBlue,imgGreen,imgRed))
cv2.imshow("window",new_img)
cv2.waitKey(0)
