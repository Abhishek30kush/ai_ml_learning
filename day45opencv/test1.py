import numpy as np
import cv2 as cv


img=cv.imread("messi.jpg")

assert img is not None, "File could not be read check, with os.path.exists()"

img[100,100] #= [255, 255, 255]
# print (img[100, 100])

print(img.shape)
print(img.size)
print(img.dtype)

# roi copy
roi = img[300:380, 420:500]

img[100:180, 490:570] = roi

# split channels
b,g,r=cv.split(img)
# merge back
img=cv.merge((b,g,r))

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()

# print(px)

# blue=img[100, 100, 0]

# print(blue)