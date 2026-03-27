import cv2 as cv
import numpy as np
# create blank white image
img=np.ones((500, 500, 3), dtype='uint8')*255

# draw 3 circles (like OpenCV logo)

# red circle 
cv.circle(img, (250, 150), 80, (0, 0, 255), -1)

# green cirlce
cv.circle(img, (150, 300), 80, (0, 255, 0), -1)

# blue cirlce
cv.circle(img, (350, 300), 80, (255, 0, 0), -1)

# Optional : draw inner smaller white circle

cv.circle(img,(250, 150), 35, (255, 255, 255), -1 )
cv.circle(img,(150, 300), 35, (255, 255, 255), -1 )
cv.circle(img,(350, 300), 35, (255, 255, 255), -1 )

cv.imshow("OpenCV Logo(Custom)", img)
cv.waitKey(0)
cv.destroyAllWindows()