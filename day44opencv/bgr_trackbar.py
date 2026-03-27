import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((400, 600, 3), np.uint8)

# Resizable window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800, 500)

# HSV trackbars
cv2.createTrackbar('H', 'image', 0, 179, nothing)
cv2.createTrackbar('S', 'image', 0, 255, nothing)
cv2.createTrackbar('V', 'image', 0, 255, nothing)

# Switch
cv2.createTrackbar('ON/OFF', 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    switch = cv2.getTrackbarPos('ON/OFF', 'image')

    if switch == 0:
        img[:] = 0
    else:
        hsv_color = np.uint8([[[h, s, v]]])
        bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)
        img[:] = bgr_color[0][0]

        # Add text
        text = f'H:{h} S:{s} V:{v}'
        cv2.putText(img, text, (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

cv2.destroyAllWindows()