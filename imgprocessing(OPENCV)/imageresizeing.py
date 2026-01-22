# i can make resizing website using opencv
import cv2
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")

#resizing the image using opencv

img_resize = cv2.resize(img,(256,256))

# half size : or any percentage change in size for example for 33 percent //3
img_resize_half = cv2.resize(img,(img.shape[1]//2, img.shape[0]//2))

cv2.imshow("window",img_resize)
cv2.waitKey(0)
print(img_resize.shape)
print(img.shape)