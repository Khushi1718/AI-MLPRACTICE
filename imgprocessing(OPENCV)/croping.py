import cv2
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")
# we will do slicing to crop the image
img_crop = img[100:300,200:400] # img[y1:y2 , x1:x2]
cv2.imshow("window",img_crop)
cv2.waitKey(0)

# how to save an image to save in future
cv2.imwrite("croped_image.jpg",img_crop)