## 
**Agente Especial:** [Tu Nombre/Matrícula]

---
## Evidencias
### Misión 1
- Imagen recuperada x50: 
- Imagen recuperada x50 + 20: 
- Código:

import cv2

import numpy as np


img = cv2.imread("m1_oscura.png", 0)

alto, ancho = img.shape


image_x50 = np.zeros((alto, ancho), dtype=np.uint8)

image_final = np.zeros((alto, ancho), dtype=np.uint8)

for i in range(alto):
    for j in range(ancho):
       
        v1 = int(img[i, j]) * 50
        
        if v1 > 255:
            v1 = 255
        elif v1 < 0:
            v1 = 0
        
        image_x50[i, j] = v1

        
        v2 = int(img[i, j]) * 50 + 20
        
        if v2 > 255:
            v2 = 255
        elif v2 < 0:
            v2 = 0
        
        image_final[i, j] = v2

cv2.imwrite("m1_recuperado_x50.png", image_x50)

cv2.imwrite("m1_recuperado_x50_mas20.png", image_final)


cv2.imshow("Imagen recuperada", image_final)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

img = cv2.imread("m1_oscura.png", 0)


image_x50 = cv2.multiply(img, 50)
cv2.imwrite("m1_recuperado_x50.png",image_x50)

image_final = cv2.add(image_x50, 20)

cv2.imwrite("m1_recuperado_x50_mas20.png", image_final)

cv2.imshow("Imagen recuperada", image_final)

cv2.waitKey(0)

cv2.destroyAllWindows()
### Misión 2
- QR reconstruido: (inserta)
- Código:
import cv2

import numpy as np

m1 = cv2.imread("m2_mitad1 1.png")

m2 = cv2.imread("m2_mitad2 1.png")

lienzo = np.ones((400,400,3), dtype=np.uint8)*255

m1 = cv2.warpAffine(m1, np.float32([[1,0,-50],[0,1,-50]]), (400,400))


h, w = m2.shape[:2]
m2 = cv2.warpAffine(m2, cv2.getRotationMatrix2D((w//2,h//2),180,1),(w,h))


lienzo[0:200,100:300] = m1[0:200,0:200]

lienzo[200:400,100:300] = m2[0:200,0:200]


cv2.imshow("QR", lienzo)

cv2.waitKey(0)

cv2.destroyAllWindows()


cv2.imwrite("m2_qr_reconstruido.png", lienzo)

### Misión 3
- Sello forjado: (inserta)
- Código:

### Misión 4
- Máscara Cyan: (inserta)
- Código:
import cv2

import numpy as np

img = cv2.imread("m4_ruido.png")


img = cv2.filter2D(img, -1, np.ones((3,3))/9)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (80,100,100), (100,255,255))


cv2.imshow("mask", mask)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite("m4_mask_cyan.png", mask)
### Misión 5
- Evidencia tricolor: (inserta)
- Mensaje recuperado: (inserta)
- Código:

---
## Análisis del Analista (Reflexiones Finales)

1. **Operadores puntuales (M1):** ¿Qué diferencia visual hay entre recuperar con multiplicación (x50) y recuperar con suma (+50)? ¿Cuál preserva mejor el contraste del texto?
> [Respuesta]

2. **Transformaciones geométricas (M2):** ¿Por qué es importante escoger el centro correcto al rotar una imagen con `getRotationMatrix2D`?
> [Respuesta]

3. **Convolución (M4):** ¿Por qué un filtro promedio puede ayudar a reducir falsos positivos antes de segmentar por HSV, y qué desventaja tiene sobre los bordes del texto?
> [Respuesta]

4. **Canales (M5):** ¿Por qué separar canales puede revelar información que en la imagen a color “no se ve” a simple vista?
> [Respuesta]