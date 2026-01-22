import cv2
import numpy as np
cap =cv2.VideoCapture(0) # 0 is my primary means my webcam

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while True:
    ret,frame=cap.read()

     # to covert it to gray scale OR OTHER FILTER KINDA THING
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)

    # for saving
    out.write(frame)

    # print(ret) # it will return true if frame is captured otherwise false

    # if not ret:
    #     print("no frame found")
    #     break

    cv2.imshow("webcam",frame) # if wanted that gray vala to frame ki jgh = img_gray

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

out.release() # releasing the video writer object

cv2.destroyAllWindows()

# # reading the saved video
# import time
# cap =cv2.VideoCapture('output.avi') 
# while True:
#     ret,frame=cap.read()

#     cv2.imshow("webcam",frame) 
#     time.sleep(1/26) # to slow down the video playback speed

#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break


# cv2.destroyAllWindows()
