import cv2 as cv
import numpy as np

canvas=np.zeros((600, 900, 3), dtype=np.uint8)

# initial settings 
drawing = False
eraser=False
ix, iy=-1, -1
color=(0, 255, 0) #default green
thickness = 5

def draw(event, x, y, flags, param):
    global ix, iy, drawing, color, thickness, eraser

    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
        ix, iy=x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if eraser:
                cv.line(canvas, (ix, iy), (x, y), (0, 0,0), thickness*2)
            else: 
                cv.line(canvas, (ix, iy), (x, y), color, thickness)
            ix, iy= x, y 
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False

cv.namedWindow("Paint App")
cv.setMouseCallback("Paint App", draw)

print("Controls: B-Blue G-Green R-Red Y-Yellow E=Eraser +-IncreaseBrushSize - - DecreaseBrushSize C-clear screen s-save image esc-exit ")

while True:
    cv.imshow("Paint App", canvas)
    key =cv.waitKey(1) & 0xFF

    if key==27: #esc
        break
    elif key==ord('b'):
        color=(255, 0, 0)
        eraser=False
    elif key==ord('g'):
        color=(0, 255, 0)
        eraser=False 
    elif key ==ord('r'):
        color=(0,0,255)
        eraser=False
    elif key==ord('y'):
        color=(0, 255, 255)
        eraser=False
    elif key==ord('e'):
        eraser=True
    elif key==ord('+'):
        thickness +=1
    elif key==ord('-'):
        thickness=max(1, thickness-1)

    elif key==ord('c'):
        canvas[:]=0

    elif key==ord('s'):
        cv.imwrite("drawing.png", canvas)
        print("Saved as drawing.png")
cv.destroyAllWindows()