import cv2
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")

# 0 : flip on vertical axis
# 1 : flip on horizontal axis
#-1 : flip on both axis

# to remove overfitting we use data augumentation technique called flipping
img_flip = cv2.flip(img,0)
cv2.imshow("window",img_flip)
cv2.waitKey(0)