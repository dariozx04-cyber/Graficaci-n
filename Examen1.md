# Examen 1

Dario Padilla Moreno

Grupo:B
## Misión 1

import cv2

import numpy as np

img = cv2.imread('m1_oscura.png')

h, w, c = img.shape

for y in range(h):

    for x in range(w):
        for k in range(c):
            img[y, x, k] = np.clip(img[y, x, k] * 50, 0, 255)

cv2.imshow("resultado", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

## Misión 3
import cv2

import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)

img[:] = (50,20,20)

cv2.circle(img, (250,250), 100, (0,255,255), 3)

cv2.rectangle(img, (200,200), (300,300), (0,0,255), -1)


cv2.line(img, (0,0), (500,500), (255,255,255), 2)

cv2.line(img, (500,0), (0,500), (255,255,255), 2)


cv2.imshow("Sello", img)

cv2.waitKey(0)

cv2.destroyAllWindows()