# Proyecto 2
Dario Padilla Moreno

## Objetivo

Crear una ciudad que se pueda manipular con Mediapipe usando geometria y parametricas

## La Escuela:

 Composición jerárquicaLa escuela la construí mediante un sistema de capas y jerarquías. Definí el cuerpo principal como una box base sobre la que fui añadiendo sub-objetos. Para mantener el orden, utilizo glPushMatrix() y glPopMatrix() cada vez que añado un detalle; esto me permite aislar las transformaciones de las ventanas y las columnas. Por ejemplo, para los pilares de la entrada, encapsulo un cyl (cilindro) y le aplico una rotación de 90° en el eje X, asegurán##dome de que solo afecte a ese pilar y no al resto de la fachada. La bandera la traté como una composición de polígonos apilados, donde calculé las coordenadas $(x, y, z)$ para colocar cada color sobre la pared frontal.

## Caminos: 
Texturizado geométricoEn lugar de aplicar una textura de imagen sobre un plano, desarrollé draw_adoquin para generar una textura procedimental.Alineación espacial: Calculé la rotación necesaria del camino usando math.atan2 sobre los puntos iniciales y finales, lo que me permite orientar cualquier tramo en el plano $XZ$ de forma precisa.Generación de detalle: Utilicé bucles anidados para iterar sobre el área del camino, dibujando bloques individuales (box) para cada adoquín. Lo que hace que esto se vea natural es que introduje una semilla fija (random.Random(99)) para variar ligeramente el tono de gris de cada bloque, rompiendo la uniformidad y simulando un desgaste realista del suelo.

## Casas:
El diseño de las casas es donde apliqué mis conocimientos de geometría:

Volumetría manual: Defino las paredes usando GL_QUADS, calculando manualmente los vértices para cerrar el volumen.

Diseño de cubiertas: Para los techos a dos aguas, integré GL_TRIANGLES para los frontones y GL_QUADS para las pendientes. La clave aquí fue calcular una variable ph (altura del techo) que define la altura del vértice central. Esto crea el efecto de pirámide truncada de forma dinámica.

Modularidad: Al encapsular toda la lógica de la casa en estas funciones, creé objetos reutilizables. Puedo instanciar una casa en cualquier punto de mi pueblo simplemente enviando las coordenadas de traslación, sin tener que preocuparme por reconstruir la geometría desde cero cada vez.

## Codigos:

def draw_escuela(x,z,rot=0):

    glPushMatrix(); glTranslatef(x,0,z); glRotatef(rot,0,1,0)
    # Cuerpo principal (Caja base)
    glColor3f(.95,.90,.72); box(-8.0,0,-5.0,8.0,4.5,5.0)
    
    # Columnas de entrada (Transformación aislada)
    for cx in [-2.0,0.0,2.0]:
        glPushMatrix(); glTranslatef(cx,0,5.01); glRotatef(-90,1,0,0)
        cyl(.22,4.5,10); glPopMatrix() # El glPopMatrix asegura que la columna no afecte a otros elementos
    
    # Bandera (Bloques de colores apilados)
    glColor3f(.22,.45,.22); box(-.70,0,5.00,.70,2.5,5.09) # Verde
    glColor3f(.95,.95,.95); box(-6.0,6.8,4.1,-4.4,7.5,4.15) # Blanco
    glColor3f(.80,0,0); box(-4.4,6.8,4.1,-2.8,7.5,4.15) # Rojo
    glPopMatrix()

 def draw_adoquin(x0,z0,x1,z1,w=2.5):

    dx,dz=x1-x0,z1-z0
    length=math.sqrt(dx*dx+dz*dz)
    ang=math.degrees(math.atan2(dx,dz)) # Cálculo de ángulo para rotar el camino
    
    glPushMatrix(); glTranslatef(x0,.005,z0); glRotatef(-ang,0,1,0)
    nr=int(length/.55); nc=int(w/.55) # Número de adoquines basados en la longitud
    rng2=random.Random(99) # Semilla constante para el "ruido" de color
    for r in range(nr):
        for c in range(nc):
            g=.44+rng2.uniform(-.04,.04) # Variación aleatoria controlada
            glColor3f(g,g-.01,g-.02)
            rx=-w/2+c*.55+.04; rz=r*.55+.04
            box(rx,.005,rz,rx+.50,.025,rz+.50) # El adoquín individual
    glPopMatrix()

def draw_house(x,z,rot=0,w=3.0,d=2.2,...):

    glPushMatrix(); glTranslatef(x,0,z); glRotatef(rot,0,1,0)
    hw=w/2; hd=d/2; H=2.6
    
    # Definición de paredes con quads
    glBegin(GL_QUADS)
    quad(-hw,0,hd,hw,0,hd,hw,H,hd,-hw,H,hd) # Frontal
    # ... (resto de paredes)
    glEnd()
    
    # Techo a dos aguas (Uso de triángulos para la pendiente)
    ph=H+1.3 # Altura de la punta
    glBegin(GL_TRIANGLES)
    glVertex3f(-hw-ext,H,hd+ext); glVertex3f(hw+ext,H,hd+ext); glVertex3f(0,ph,0)
    glEnd()
    glPopMatrix()

## Conclusion fianl
Este proyecto demuestra que no necesitas herramientas externas complejas para crear un mundo 3D funcional. Al combinar la geometría analítica (para construir los edificios), la generación procedimental (para los detalles de los caminos) y la integración de visión artificial (para controlar la cámara con gestos), logre crear un sistema eficiente