# Actividad isometrica
Dario Padilla Moreno

Grupo: B

Se realizó una figura isométrica de cubos utilizando OpenCV, donde primero se cree un cuadrado que representa la cara frontal. Después, ese cuadrado se desplazó en diagonal para simular profundidad y formar las caras superior y lateral. Finalmente conecte los puntos con líneas y se repeti el proceso en diferentes posiciones

## CÓDIGO
import cv2
import numpy as np

img = np.zeros((600, 600, 3), dtype=np.uint8)


def cubo(x, y, s=60):

    dx = s // 2

    dy = s // 2

    p1 = (x, y)
    p2 = (x + s, y)
    p3 = (x + s, y + s)
    p4 = (x, y + s)

   
    p5 = (x + dx, y - dy)
    p6 = (x + s + dx, y - dy)

   
    p7 = (x + s + dx, y + s - dy)


    cv2.line(img, p1, p2, (255,255,255), 2)
    cv2.line(img, p2, p3, (255,255,255), 2)
    cv2.line(img, p3, p4, (255,255,255), 2)
    cv2.line(img, p4, p1, (255,255,255), 2)

   
    cv2.line(img, p1, p5, (255,255,255), 2)
    cv2.line(img, p2, p6, (255,255,255), 2)
    cv2.line(img, p5, p6, (255,255,255), 2)

    
    cv2.line(img, p2, p6, (255,255,255), 2)
    cv2.line(img, p6, p7, (255,255,255), 2)
    cv2.line(img, p7, p3, (255,255,255), 2)




cubo(200, 400)
cubo(260, 400)
cubo(320, 400)

cubo(230, 340)
cubo(290, 340)


cubo(260, 280)


cv2.imshow("Figura Isometrica de Cubos", img)

cv2.waitKey(0)

cv2.destroyAllWindows()