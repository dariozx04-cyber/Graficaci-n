# Puntos caracteristicos en Realidada Aumentada
Dario Padilla Moreno
## Puntos caracteristicos
Son píxeles o regiones de una imagen que tienen un patrón único y fácilmente reconocible, como esquinas, bordes o texturas distintivas.
Ejemplos: esquinas de un edificio, marcas en una superficie, intersecciones de líneas.

Los algoritmos de puntos característicos sirven para encontrar pistas visuales únicas en una imagen que el sistema puede rastrear aunque la cámara se mueva, cambie la luz o se rote el objeto.

- Características principales de los algoritmos de puntos característicos


**Invariancia**

Escala: El punto debe detectarse aunque la imagen esté ampliada o reducida.
Rotación: El punto debe detectarse aunque la imagen esté girada.
Iluminación: Debe ser robusto a cambios de brillo y contraste.



**Repetibilidad**

El mismo punto debe detectarse en diferentes tomas de la misma escena.



**Precisión de localización**

La posición del punto debe calcularse con exactitud subpíxel.



**Distintividad**

El descriptor del punto debe diferenciarlo claramente de otros puntos.



**Eficiencia computacional**

El algoritmo debe ser rápido y escalable para imágenes grandes o video en tiempo real.



**Robustez al ruido**

Debe funcionar incluso si la imagen tiene ruido o compresión.




- **Ejemplos de algoritmos de puntos característicos:**



| Algoritmo | Tipo | Ventajas | Desventajas |
|-----------|------|----------|-------------|
| **Harris Corner Detector** | Detector | Simple y rápido | No es invariante a escala |
| **SIFT** (Scale-Invariant Feature Transform) | Detector + Descriptor | Invariante a escala y rotación, muy robusto | Más lento, antes tenía patente (ya expirada) |
| **SURF** (Speeded-Up Robust Features) | Detector + Descriptor | Más rápido que SIFT, robusto a cambios de iluminación | Menos preciso en algunos casos |
| **ORB** (Oriented FAST and Rotated BRIEF) | Detector + Descriptor | Muy rápido, libre de patentes | Menos robusto que SIFT en cambios extremos |
| **FAST** (Features from Accelerated Segment Test) | Detector | Extremadamente rápido | No genera descriptores por sí mismo |

## En Realidada Aumentada
1.Detección y Extracción:El algoritmo analiza el flujo de video buscando esquinas o contrastes estables mediante detectores rápidos como FAST o ORB. Cada punto recibe un descriptor

2.Emparejamiento:Se comparan los descriptores del cuadro actual con los del cuadro anterior .Algoritmos como Brute-Force Matcher o FLANN calculan cuáles puntos coinciden entre sí.

3.Filtro de Ruido:No todas las coincidencias son correctas debido a reflejos o desenfoque. Se aplica RANSAC para descartar falsos positivos y quedarse solo con los puntos que se mueven de manera coherente.

4.Estimación de la Pose:Al conocer las coordenadas 2D de los puntos en la pantalla y mapearlas a sus coordenadas 3D en el espacio real, se resuelve el problema de Perspectiva desde N Puntos . Esto calcula la matriz de rotación y traslación de la cámara.
## En Aprendizaje Maquina
Tradicionalmente, los puntos característicos eran algoritmos matemáticos manuales, pero el ML ha evolucionado el área de dos maneras:

## Sustitución de algoritmos clásicos por Redes Neuronales

En lugar de usar fórmulas fijas para buscar esquinas, se entrenan redes neuronales convolucionales (CNN) para que aprendan autónomamente qué partes de una imagen son las mejores para rastrear.

SuperPoint: Una red neuronal que detecta puntos de interés y calcula sus descriptores al mismo tiempo. Es muchísimo más resistente a cambios drásticos de iluminación o clima que los métodos tradicionales.

SuperGlue: Un modelo de aprendizaje profundo que utiliza mecanismos de atención para hacer el matching  de puntos entre imágenes, logrando una precisión impresionante en escenarios complejos.

## Reducción de dimensiones y Clasificación
Si estás entrenando un modelo clásico de ML para clasificar objetos o rostros, pasarle la imagen cruda píxel por píxel requiere demasiado poder de cómputo y genera ruido.

Usas un algoritmo como SIFT o ORB para extraer los puntos clave.

Agrupas esos descriptores usando técnicas como Bag of Visual Words (BoVW) para crear un vector compacto de características.

Le entregas este vector procesado a tu modelo de Machine Learning, el cual aprenderá a clasificar el objeto mucho más rápido.