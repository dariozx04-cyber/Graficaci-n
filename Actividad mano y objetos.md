# Actividad de manos y objetos

Dario Padilla Moreno

Grupo:B

Lo que hice primero fue definir las coordenadas iniciales para cada figura  lo que permitió que aparecieran en la pantalla.

Después se usaron las funciones de dibujo de OpenCV para crear cada figura:

cv2.circle() para el círculo

cv2.rectangle() para el cuadrado

cv2.polylines() para el triángulo

El tamaño de las figuras se controló utilizando la distancia entre el pulgar y el dedo índice, que se calculó con los landmarks de la mano.

## Codigo

import cv2

import mediapipe as mp

import numpy as np

import math

BaseOptions = mp.tasks.BaseOptions

HandLandmarker = mp.tasks.vision.HandLandmarker

HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions

VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)


HAND_CONNECTIONS = [
(0,1),(1,2),(2,3),(3,4),
(0,5),(5,6),(6,7),(7,8),
(5,9),(9,10),(10,11),(11,12),
(9,13),(13,14),(14,15),(15,16),
(13,17),(0,17),(17,18),(18,19),(19,20)
]

cap = cv2.VideoCapture(0)


x_cir,y_cir = 200,200

x_cua,y_cua = 400,200

x_tri,y_tri = 300,400

distancia = 40

with HandLandmarker.create_from_options(options) as landmarker:

    while cap.isOpened():

        ret,frame = cap.read()
        if not ret:
            break

        h,w,_ = frame.shape

        frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data=frame_rgb)

        results = landmarker.detect(mp_image)

        if results.hand_landmarks:

            for hand_landmarks in results.hand_landmarks:

                keypoints=[]

                for lm in hand_landmarks:

                    cx=int(lm.x*w)
                    cy=int(lm.y*h)

                    keypoints.append((cx,cy))

                    cv2.circle(frame,(cx,cy),5,(255,0,0),-1)

                # dibujar lineas de la mano
                for con in HAND_CONNECTIONS:
                    cv2.line(frame,
                             keypoints[con[0]],
                             keypoints[con[1]],
                             (0,255,0),2)

                # pulgar e indice
                x1,y1 = keypoints[4]
                x2,y2 = keypoints[8]

                cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),3)

                distancia = int(math.hypot(x2-x1,y2-y1))

                # mover figuras si el dedo las toca
                if math.hypot(x2-x_cir,y2-y_cir)<distancia:
                    x_cir,y_cir = x2,y2

                if abs(x2-x_cua)<distancia and abs(y2-y_cua)<distancia:
                    x_cua,y_cua = x2,y2

                if math.hypot(x2-x_tri,y2-y_tri)<distancia:
                    x_tri,y_tri = x2,y2

        # circulo
        cv2.circle(frame,(x_cir,y_cir),distancia,(255,0,0),2)

        # cuadrado
        cv2.rectangle(frame,
                      (x_cua-distancia,y_cua-distancia),
                      (x_cua+distancia,y_cua+distancia),
                      (0,255,0),2)

        # triangulo
        pts=np.array([
            (x_tri,y_tri-distancia),
            (x_tri-distancia,y_tri+distancia),
            (x_tri+distancia,y_tri+distancia)
        ])

        cv2.polylines(frame,[pts],True,(0,0,255),2)

        cv2.imshow("Salida",frame)

        if cv2.waitKey(1)&0xFF==ord('q'):
            break

cap.release()

cv2.destroyAllWindows()