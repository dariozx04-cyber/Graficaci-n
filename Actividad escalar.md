## Actividad escalar

Dario Padilla Moreno

Grupo:B

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\OIP.png" width="200" height= "200">

 Inicialmente, al aumentar el tamaño de la imagen solo se copiaban los píxeles originales en nuevas posiciones, lo que provocaba que quedaran espacios vacíos con valor 0  entre ellos.

Para solucionar este problema, se implementaron ciclos for adicionales que permitieron rellenar esos espacios repitiendo cada píxel original en un bloque del tamaño del factor de escala.

import cv2 as cv

import numpy as np



img = cv.imread('OIP.png', 0)


x, y = img.shape

scale_x, scale_y = 2, 2

scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

for i in range(x):
    for j in range(y):
                  for dx in range(scale_x):
                    for dy in range(scale_y):
                        scaled_img[i*scale_x + dx, j*scale_y + dy] = img[i, j]


cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()