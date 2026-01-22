import cv2 
import numpy as np 
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")

flag = False
ix=-1
iy=-1
def algo(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        flag=True
        ix=x
        iy=y

    elif event==4:
        flag=False
        fx=x
        fy=y
        #cropping the image
        cropped=img[iy:fy,ix:fx]
        # cv2.imshow("new_window",cropped)
        # cv2.waitKey(0)
        cv2.imwrite("cropped.jpg",cropped)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",algo)
while True:
    cv2.imshow("window",img)
    if(cv2.waitKey(1) & 0xFF==ord('x')):
        break
cv2.destroyAllWindows()

