import cv2
import numpy as np
# creating a image 
img = np.zeros((512,512,3))

# rectangle 255,0,0 is blue color in BGR
# thickness -1 means filled rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)
#circle
cv2.circle(img,center=(300,300),radius=50,color=(0,255,0),thickness=5)
#line
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(0,0,255),thickness=5)
#text
cv2.putText(img,text="OpenCV",org=(400,400),
fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA ,fontFace=cv2.FONT_ITALIC)

cv2.imshow("window",img)
cv2.waitKey(0)