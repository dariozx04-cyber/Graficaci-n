Dario Padilla Moreno

Grupo:B
## Actividad 1
import cv2

import numpy as np


img = cv2.imread('frutas.png')


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_green = np.array([35, 100, 100])  
upper_green = np.array([85, 255, 255])  

mask = cv2.inRange(hsv, lower_green, upper_green)

result = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow("Imagen Original", img)

cv2.imshow("Color Detectado", result)

cv2.waitKey(0)

cv2.destroyAllWindows()
## Actividad 2
import cv2

import numpy as np

img = cv2.imread('frutas.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 100, 100])

upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

cv2.imshow("Mascara sin limpiar", mask)

kernel = np.ones((5,5), np.uint8)

mask_limpia = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow("Mascara limpia", mask_limpia)

cv2.waitKey(0)

cv2.destroyAllWindows()
## Actividad 3
import cv2

import numpy as np

img = cv2.imread('frutas.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_green = np.array([35, 100, 100])

upper_green = np.array([85, 255, 255])


mask = cv2.inRange(hsv, lower_green, upper_green)

cv2.imshow("Mascara sin limpiar", mask)

kernel = np.ones((5,5), np.uint8)


mask_limpia = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow("Mascara limpia", mask_limpia)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask_limpia)

area_min = 500

contador = 0

for i in range(1, num_labels): 

    area = stats[i, cv2.CC_STAT_AREA]
    if area > area_min:
        contador += 1
        print("Fruta",{contador}, "Area:",{area} )

print("Total frutas verdes detectadas:", contador)

cv2.waitKey(0)

cv2.destroyAllWindows()
## Actividad 4
import cv2

import numpy as np


img = cv2.imread('frutas.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

kernel = np.ones((5,5), np.uint8)

area_min = 500  


def contar_frutas(mask, color_nombre):
   
    mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask_clean)

    contador = 0
    print("\nColor:", color_nombre)

    for i in range(1, num_labels):  # 0 es fondo
        area = stats[i, cv2.CC_STAT_AREA]
        if area > area_min:
            contador += 1
            print("Fruta", contador, "- Area:", area)

    print("Total", color_nombre, ":", contador)
    return contador



lower_red= np.array([0, 100, 100])

upper_red = np.array([10, 255, 255])

lower_red2 = np.array([170,120,70])

upper_red2 = np.array([180,255,255])

mask_red1 = cv2.inRange(hsv, lower_red, upper_red)

mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask_red = mask_red1 + mask_red2



result1 = cv2.bitwise_and(img, img, mask=mask_red,)


rojo_total = contar_frutas(mask_red, "Rojo")



lower_green = np.array([35, 100, 100])

upper_green = np.array([85, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)

verde_total = contar_frutas(mask_green, "Verde")

result2 = cv2.bitwise_and(img, img,mask=mask_green)


lower_yellow = np.array([20, 100, 100])

upper_yellow = np.array([35, 255, 255])

mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

amarillo_total = contar_frutas(mask_yellow, "Amarillo")

result3 = cv2.bitwise_and(img, img,mask=mask_yellow)

cv2.imshow("Imagen Original", img)

cv2.imshow("Color Rojo",result1 )

cv2.imshow("Color Verde",result2 )

cv2.imshow("Color Amarillo",result3 )

cv2.waitKey(0)

cv2.destroyAllWindows()


