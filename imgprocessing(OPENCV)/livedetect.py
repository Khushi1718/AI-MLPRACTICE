import cv2
import numpy as np

# creating a image 
img = np.zeros((512,512,3), dtype=np.uint8)

# so now we need to make a event listner the moment mouse click it trigger a particular function 
def draw(event,x,y,flags,params):
    print("eventTriggered")
    print(event) # 0 on hower click 1 and leaving after click 4
    if event == 0:
        print("mouse moved")
    elif event == 1:
        print("mouse down click")
        cv2.circle(img,center=(x,y),radius=10,color=(0,255,0),thickness=-1)
    else:
        print("mouse up click")

cv2.namedWindow(winname="window")
# window and fun : draw
cv2.setMouseCallback("window", draw)

#events:we click on the image a event happen like a circle will draw 

# this is infinte loop to see the image repeatedly
while True:
    cv2.imshow("window", img)
    
    # it says if a image on screen for a sec and we press x then close the image
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
