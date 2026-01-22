import cv2
print(cv2.__version__)

#images are of 3 type simplest is black and white 0 - 1
# grayscale images here 0 is black 255 is white so we have range from 0 to 255
# coloured images - we use 3 channels whicha re rgb
# resolution is the pixcles in the sheets of pixel 

#read the image 

img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")
print(img)
print(type(img))
print(img.shape)

# how to display 
# cv2.imshow("window",img)
#delay the close of image to infinte
# cv2.waitKey(0)

# convert BGR → RGB for colab
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.axis('off')

# how to convert a rgb image to grey scale image 
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window",img_gray)
cv2.waitKey(0)
print(img_gray.shape)