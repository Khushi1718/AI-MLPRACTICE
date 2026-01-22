# • Upload an image to your Colab environment.
# • Load and display the image.
# • Convert the image from BGR to RGB format.
# • Resize the image to a standard shape (e.g., 128×128 pixels).
# • Convert the image to grayscale.
# • Convert the grayscale image to binary using thresholding.
# • Normalize the image pixel values.
# • Apply basic augmentations like flipping and rotating the image.
# • Apply filters to remove noise such as Gaussian or median blur.
# • Flatten the image and display the new shape.

import cv2
import numpy as np 
img = cv2.imread("imgprocessing(OPENCV)/ -3.jpg")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# Resize to 128x128
img_resized = cv2.resize(img_rgb, (128,128))
# Convert to Grayscale
img_gray = cv2.cvtColor(img_resized, cv2.COLOR_RGB2GRAY)
# Convert to Binary using Thresholding
_, img_binary = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# Normalize pixel values
img_normalized = img_binary / 255.0
# Apply Flipping
img_h= cv2.flip(img_normalized, 1) # Horizontal flip
img_v= cv2.flip(img_normalized, 0) # Vertical flip
# Apply Rotation
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# Apply Gaussian Blur
# cv2.GaussianBlur(src, ksize, sigmaX) KSIZE = KERNEL SIZE AND SIGMAX = STANDARD DEVIATION IN X DIRECTION(BLUR INTENSITY)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
# Apply Median Blur
median = cv2.medianBlur(img, 5)
# Flatten the image  (Flattening converts a 2D image into a 1D feature vector for machine learning models)   
flattened = img_normalized.flatten()
print("New shape after flattening:", flattened.shape)
while True:
    cv2.imshow("window",img)
    if(cv2.waitKey(1) & 0xFF==ord('x')):
        break
cv2.destroyAllWindows()



