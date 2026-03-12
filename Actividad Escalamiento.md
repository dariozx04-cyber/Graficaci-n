# Actividad 3

Dario Padilla Moreno

Grupo: B

En este programa cargue una imagen y recorte una región central de 200×200 píxeles. Después se creó un lienzo nuevo de 1000×1000 y, usando ciclos for, se calcularon las coordenadas correspondientes del recorte para copiar cada píxel. De esta forma se agrandó la imagen manualmente usando matemáticas, produciendo un efecto pixelado tipo vecino más cercano.
import cv2

import numpy as np


img = cv2.imread('microfilm.jpg')

h, w = img.shape[:2]

cx = w // 2
cy = h // 2


crop = img[cy-100:cy+100, cx-100:cx+100]


dest = np.zeros((1000,1000,3), dtype=np.uint8)


ch, cw = crop.shape[:2]


scale_x = cw / 1000

scale_y = ch / 1000


for y in range(1000):
    for x in range(1000):

        orig_x = int(x * scale_x)
        orig_y = int(y * scale_y)

    
        dest[y, x] = crop[orig_y, orig_x]

cv2.imshow("recorte", crop)

cv2.imshow("zoom_manual", dest)

cv2.waitKey(0)

cv2.destroyAllWindows()