## Actividad pinpong

Dario Padilla Moreno

Grupo B
Lo que hice fue hacer mas que nada pedir algo de ayuda de como funcionaba en si el codigo que nos dieron en clase junto con algunas operaciones magtematicas y tutoriales en internet solo  para poder guiarme para realizar la actividad.

import cv2 as cv

import numpy as np

img= np.ones ((500,500,3), np.uint8)*255

x, y = 100, 100   
dx, dy = 5, 5    
radio = 20

for i in range(1000):  
    img = np.ones((500,500,3), np.uint8) * 255
    
    cv.circle(img, (x,y), radio, (255,0,0), -1)
    
    x += dx
    y += dy
    
   
    if x <= radio or x >= 500 - radio:
        dx = -dx
    
    
    if y <= radio or y >= 500 - radio:
        dy = -dy
    
    cv.imshow("img", img)
    cv.waitKey(20)


cv.waitKey(0)

cv.destroyAllWindows()