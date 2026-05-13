# Reporte de Misión: Órbita Dual (Cámara vs Objeto)
**Agente Especial:** [Dario Padilla Moreno/24120393]
---
## Evidencias
### Misión 1
- Objeto rota: 

<img        
    src="C:\\Users\\jaime\\OneDrive\\Escritorio\\tareasGrafi\\Modo 1.png" width="200" height= "200">


- Cámara orbita:

<img        
    src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Modo2.png" width="200" height= "200">
- Código:

import glfw

from OpenGL.GL import *

from OpenGL.GLU import *

WIDTH = 800

HEIGHT = 600

CAM_DISTANCE = 8

ANGLE_SPEED = 0.5

angle = 0.0

modo = 1

quadric = None


def init():

    global quadric

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, WIDTH / HEIGHT, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)

    quadric = gluNewQuadric()


def draw_axes():

    glBegin(GL_LINES)

    # X rojo
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(3, 0, 0)

    # Y verde
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 3, 0)

    # Z azul
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 3)

    glEnd()


def draw_sphere():

    glColor3f(1, 1, 0)

    gluSphere(quadric, 1.5, 32, 32)


def render_rotating_object(angle):

    glLoadIdentity()

    # Cámara fija
    glTranslatef(0, 0, -CAM_DISTANCE)

    draw_axes()

    # Objeto rota
    glRotatef(angle, 0, 1, 0)

    draw_sphere()


def render_orbiting_camera(angle):

    glLoadIdentity()

    # Cámara orbita
    glRotatef(-angle, 0, 1, 0)

    glTranslatef(0, 0, -CAM_DISTANCE)

    draw_axes()

    # Objeto fijo
    draw_sphere()


def render_orbiting_camera_variant_b(angle):

    glLoadIdentity()

    # Variante B
    glTranslatef(0, 0, -CAM_DISTANCE)

    glRotatef(-angle, 0, 1, 0)

    draw_axes()

    draw_sphere()


def key_callback(window, key, scancode, action, mods):

    global modo

    if action == glfw.PRESS:

        if key == glfw.KEY_1:
            modo = 1

        elif key == glfw.KEY_2:
            modo = 2

        elif key == glfw.KEY_3:
            modo = 3

        elif key == glfw.KEY_ESCAPE or key == glfw.KEY_Q:
            glfw.set_window_should_close(window, True)


def main():

    global angle

    if not glfw.init():
        return

    window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "Operacion Orbita Dual",
        None,
        None
    )

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_callback)

    init()

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)

        if modo == 1:
            render_rotating_object(angle)

        elif modo == 2:
            render_orbiting_camera(angle)

        elif modo == 3:
            render_orbiting_camera_variant_b(angle)

        angle += ANGLE_SPEED

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
### Misión 2
- LookAt órbita: (inserta imagen)
- Código:

### Misión 3 (opcional)
- Luces: (inserta)
- Notas:

---
## Análisis del Analista (Reflexiones Finales)

1. **Orden de matrices:** ¿Por qué en OpenGL fijo el orden en que escribes =glTranslatef= / =glRotatef= cambia el resultado aunque uses los mismos números?
> Porque OpenGL multiplica las matrices en orden inverso al que se escriben.

2. **Objeto vs cámara:** En la práctica, ¿cuándo prefieres rotar el modelo y cuándo orbitar la cámara?
> Rotar el modelo se usa cuando queremos mostrar el objeto girando sobre sí mismo y orbitar la cámara se usa cuando el objeto debe permanecer fijo y queremos observarlo desde diferentes ángulos
3. **gluLookAt vs translate+rotate:** ¿Qué ventaja tiene describir la cámara con ojo–objetivo–arriba para equipos de desarrollo?
> [Respuesta]

4. **Luces:** Si la luz se define en el frame de la cámara sin reubicarla al mundo, ¿qué artefacto visual esperas al rotar solo el objeto?
> [Respuesta]
