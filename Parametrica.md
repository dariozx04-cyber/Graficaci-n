# Actividad Parametrica
Dario Padilla Moreno
GrupoB

Esta actividad encontre la solucion en simplemente reutilizar el codigo que ya habian en los apuntes, lo unico que hice fue agregar más funciones parametricas y cambiar coordenadas.

<img src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Parametricadib.png" width="200" height= "200">

## Código
import numpy as np

import cv2
 
width, height = 1000, 1000  

img = np.ones((height, width, 3), dtype=np.uint8)*255


#Parámetros de la curva de Limacon

a, b = 150, 100 

a2,b2= 100, 95

a3,b3=100, 95 

a4,b4=50,50
 
k = 1.9

k2=0.65

k3=1.8

k4=2.5 

theta_increment = 0.05  

max_theta = 2 * np.pi 


center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial

while True:  # Bucle infinito
   
    
    # Dibujar la curva completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        
        r = a + b * np.cos(k * t)
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))

        r2 = a2 + b2 * np.cos(k2 * t)
        x2 = int(center_x + r2 * np.cos(t))
        y2 = int(center_y + r2 * np.sin(t))
        
        r3 = a3 + b3 * np.cos(k3 * t)
        x3 = int(center_x + r3 * np.cos(t))
        y3 = int(center_y + r3 * np.sin(t))
        
        r4 = a4 + b4 * np.cos(k4 * t)
        x4 = int(center_x + r4 * np.cos(t))
        y4 = int(center_y + r4 * np.sin(t))
        
        # Dibujar un círculo en la posición calculada
        #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
        cv2.circle(img, (x-2, y-2), 3, (0, 0, 0), -1)  # Color rojo
        cv2.circle(img, (x2+100, y2+100), 3, (0, 0, 0), -1) 
        cv2.circle(img, (x3-100, y3-100), 3, (0, 0, 0), -1) 
        cv2.circle(img, (x4+150, y4+150), 3, (0, 0, 0), -1) 
    # Mostrar la constante k en la imagen
    #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Mostrar la imagen
    cv2.imshow("Parametric Animation", img)

    #img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Reiniciar theta si alcanza su valor máximo
    #if theta >= max_theta:
    #    theta = 0  # Reinicia la animación para que se repita

    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

 
cv2.destroyAllWindows()

