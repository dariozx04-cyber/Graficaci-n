## 
**Agente Especial:** [Tu Nombre/Matrícula]

---
## Evidencias
### Misión 1
- Imagen recuperada x50: 

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\m1_recuperado_x50.png" width="200" height= "200">

- Imagen recuperada x50 + 20: 

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\m1_recuperado_x50_mas20.png" width="200" height= "200">

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
- QR reconstruido:

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\QR.png" width="200" height= "200">

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
- Sello forjado: <img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Mision3.png" width="200" height= "200">
- Código:
import cv2

import numpy as np

import math


img = np.zeros((600,600,3), np.uint8)

img[:] = (40,20,20)


c = (300,300)

cv2.circle(img, c, 170, (0,255,255), 3)

cv2.circle(img, c, 110, (0,255,255), 2)

cv2.rectangle(img, (250,260), (350,340), (0,0,255), -1)


cv2.line(img, (0,0), (599,599), (255,255,255), 2)

cv2.line(img, (599,0), (0,599), (255,255,255), 2)


for i in range(8):

    ang = i * 45  
    x = int(300 + 140 * math.cos(math.radians(ang)))
    y = int(300 + 140 * math.sin(math.radians(ang)))
    cv2.circle(img, (x,y), 8, (0,255,0), -1)

cv2.putText(img, "SECTOR-9", (200,560), 0, 1, (255,255,255), 2)


cv2.imwrite("m3_sello_forjado_v2.png", img)

cv2.imshow("img", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

### Misión 4
- Máscara Cyan: 

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Ruido.png" width="200" height= "200">

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
- Evidencia tricolor: 
<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\mision5.png" width="200" height= "200">
- Mensaje recuperado:
- Código:
import cv2

import numpy as np

img = np.random.randint(0,256,(300,700,3),dtype=np.uint8)

texto = "Hola"

cv2.putText(img, texto, (50,150), 0, 2, (0,255,0), 3)  


cv2.imwrite("m5_tricolor.png", img)

B, G, R = cv2.split(img)

cv2.imshow("Canal B", B)

cv2.imshow("Canal G", G)

cv2.imshow("Canal R", R)


diff = cv2.absdiff(G, B)

cv2.imshow("abs(G-B)", diff)

cv2.imwrite("m5_mensaje.png", diff)

cv2.waitKey(0)

cv2.destroyAllWindows()

---
## Análisis del Analista (Reflexiones Finales)

1. **Operadores puntuales (M1):** ¿Qué diferencia visual hay entre recuperar con multiplicación (x50) y recuperar con suma (+50)? ¿Cuál preserva mejor el contraste del texto?
> ## Multiplicación (x50)
Aumenta proporcionalmente todos los valores.
Las zonas claras se vuelven mucho más claras y las oscuras siguen siendo oscuras.
## Suma de 50
Desplaza todos los valores por igual.
Todo se vuelve más claro, pero las diferencias entre píxeles se mantienen iguales. 

2. **Transformaciones geométricas (M2):** ¿Por qué es importante escoger el centro correcto al rotar una imagen con `getRotationMatrix2D`?

> Porque el centro de rotación define alrededor de qué punto gira toda la imagen.

3. **Convolución (M4):** ¿Por qué un filtro promedio puede ayudar a reducir falsos positivos antes de segmentar por HSV, y qué desventaja tiene sobre los bordes del texto?
>
Suaviza la imagen eliminando ruido y variaciones pequeñas de color y pierde nitidez en los bordes como desventaja.

4. **Canales (M5):** ¿Por qué separar canales puede revelar información que en la imagen a color “no se ve” a simple vista?
> 
Porque cada canal guarda información distinta de la imagen. Al verlos por separado, puedes notar cosas que en la imagen a color quedan mezcladas