#  Reporte de Misión: Graficación Táctica
**Agente Especial:** Dario Padilla Moreno 24120393

---
##  Evidencias de Misión
## Mision 1
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

## MISIÓN 2

import cv2

import numpy as np

mitad1 = cv2.imread('m2_mitad1.png')

mitad2 = cv2.imread('m2_mitad2.png')

lienzo = np.zeros((400,400,3), np.uint8)


M = np.float32([[1,0,0],
                [0,1,0]])

mitad1 = cv2.warpAffine(mitad1, M, (400,200))


h, w = mitad2.shape[:2]

R = np.float32([[-1,0,w],
                [0,-1,h]])

mitad2 = cv2.warpAffine(mitad2, R, (400,200))


lienzo[0:200,0:400] = mitad1

lienzo[200:400,0:400] = mitad2

cv2.imshow("QR reconstruido", lienzo)

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

## Misión 4
import cv2

import numpy as np

img = cv2.imread('m4_ruido.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

bajo = np.array([80,100,100])

alto = np.array([100,255,255])


mascara = cv2.inRange(hsv, bajo, alto)


cv2.imshow("Mascara Cyan", mascara)

cv2.waitKey(0)

cv2.destroyAllWindows()

## MISION 5

import cv2

import numpy as np

img = np.zeros((500,500,3), dtype=np.uint8)

t = 0

while t <= 6.28:  
    
    x = int(250 + 150 * np.sin(3*t))

    y = int(250 + 150 * np.sin(2*t))
    
    cv2.circle(img, (x,y), 1, (255,255,255), -1)
    
    t += 0.01

cv2.imshow("Antena", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

---
##  Análisis del Analista (Reflexiones Finales)

1. **Sobre los Operadores Puntuales (Misión 1):** Matemáticamente, ¿qué pasaría si en lugar de multiplicar por 50, hubieras sumado 50 a cada píxel oscuro? ¿Se revelaría el texto igual de claro o la imagen perdería contraste?
> Si en lugar de multiplicar por 50 se sumara 50 a cada píxel, el texto no se veria tan claro.
Al sumar 50 todos los valores de los píxeles aumentarían casi igual, por lo que la diferencia entre los píxeles oscuros y claros sería pequeña

2. **Sobre el Espacio HSV (Misión 4):** ¿Por qué el modelo de color BGR es ineficiente para la Recuperación de Información cuando buscamos "todos los tonos de azul celeste", y por qué el modelo HSV resuelve este problema con una sola variable?
> Es ineficiente para buscar colores como el azul celeste porque el color se define con tres valores mezclados (azul, verde y rojo). Esto hace que se más difícil encontrar todos los tonos similares, ya que pequeñas variaciones cambian los tres valores. 
Y el modelo HSV representa 3 cosas
H (Hue / Matiz): el color puro

S (Saturación): intensidad del color

V (Valor): brillo
Y solo se necesita un rango en la varieble Hue.

3. **Sobre Ecuaciones Paramétricas (Misión 5):** ¿Por qué las ecuaciones paramétricas (usando el parámetro t) son mejores para dibujar formas cerradas y complejas en graficación por computadora que usar la clásica función $y=f(x)$?
> Las ecuaciones paramétricas usan un parámetro t que controla simultáneamente las coordenadas x(t) y y(t). Esto permite dibujar curvas cerradas fácilmente
