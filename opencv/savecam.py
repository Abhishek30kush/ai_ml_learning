import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)

# define the codec and create videoWriter object
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('output.avi', fourcc, 20.0, (640, 680))

while cap.isOpened():
    ret, frame=cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting....")
        break

    frame = cv.flip(frame,0)
    # write the flipped frame 
    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1)==ord('e'):
        break

cap.release()
out.release()
cv.destroyAllWindows()