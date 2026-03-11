import cv2
import numpy as np

img = cv2.imread('vehiculo.jpg')

h, w, c = img.shape


canvas = np.zeros((600, 800, 3), dtype=np.uint8)


dx = 300
dy = 200

for y in range(h):
    for x in range(w):

        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 800 and 0 <= new_y < 600:
            canvas[new_y, new_x] = img[y, x]

cv2.imshow("resultado", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()