## Actividad Dibujo
Dario Padilla Moreno

Grupo B

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Captura de pantalla 2026-02-25 213411.png" width="200" height= "200">

import cv2 as cv

import numpy as np

img = np.ones((300,500,3), np.uint8)*255


cv.rectangle(img, (80,150), (420,220), (0,0,255), -1)


cv.rectangle(img, (180,100), (320,150), (0,0,255), -1)


cv.circle(img, (165,245), 35, (0,0,0), -1)

cv.circle(img, (335,245), 35, (0,0,0), -1)


cv.circle(img, (165,245), 15, (200,200,200), -1)

cv.circle(img, (335,245), 15, (200,200,200), -1)

cv.imshow("Auto", img)

cv.waitKey(0)

cv.destroyAllWindows()