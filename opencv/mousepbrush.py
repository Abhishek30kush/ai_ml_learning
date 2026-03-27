import numpy as np 
import cv2 as cv

# mouse callback function 
def draw_cricle(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img, (x, y), 100, (255, 0, 0), -1)
# create a black image,a window and bind the function to window

img=np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_cricle)

while(1):
    cv.imshow("image", img)

    key=cv.waitKey(1) & 0xFF

    if key==27:
        break
    elif key==ord('c'): #press 'c' to clear screen
         img[:]=255
cv.destroyAllWindows()