import cv2
import numpy as np
import math

img = cv2.imread("qr_rotado.jpg")

h, w = img.shape[:2]


dest = np.zeros((h, w, 3), dtype=np.uint8)

cx = w // 2
cy = h // 2


angulo = 315
theta = math.radians(angulo)

cos_t = math.cos(theta)
sin_t = math.sin(theta)

for y in range(h):
    for x in range(w):

       
        xr = x - cx
        yr = y - cy

        x_orig = int(cos_t * xr + sin_t * yr + cx)
        y_orig = int(-sin_t * xr + cos_t * yr + cy)

       
        if 0 <= x_orig < w and 0 <= y_orig < h:
            dest[y, x] = img[y_orig, x_orig]

cv2.imshow("original", img)
cv2.imshow("corregida", dest)

cv2.waitKey(0)
cv2.destroyAllWindows()