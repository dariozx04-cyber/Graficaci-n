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
- LookAt órbita: 

<img        
    src="C:\Users\jaime\OneDrive\Escritorio\tareasGrafi\Mision 2.png" width="200" height= "200">
- Código:
from __future__ import annotations

import math
import sys

import glfw
from OpenGL.GL import *
from OpenGL.GLU import (
    GLU_FILL,
    gluLookAt,
    gluNewQuadric,
    gluPerspective,
    gluQuadricDrawStyle,
    gluSphere,
)

WINDOW_TITLE = "Orbita Dual (GLFW) — 1/2/3 cambia modo"

INITIAL_MODE = 1

ORBIT_RADIUS = 5.0
CAM_DISTANCE = 5.0
ANGLE_SPEED = 0.6

USE_LIGHTING = True

_quadric = None


def draw_sphere(radius: float = 1.0) -> None:

    global _quadric

    if _quadric is None:

        _quadric = gluNewQuadric()

        gluQuadricDrawStyle(_quadric, GLU_FILL)

    gluSphere(_quadric, radius, 40, 24)


def setup_basic_lighting() -> None:

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    pos = [2.0, 2.0, 2.0, 1.0]

    ambient = [0.2, 0.2, 0.2, 1.0]

    diffuse = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)


def render_rotating_object(angle: float) -> None:

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glTranslatef(0.0, 0.0, -CAM_DISTANCE)

    if USE_LIGHTING:
        setup_basic_lighting()

    glRotatef(angle, 0.0, 1.0, 0.0)

    glColor3f(0.35, 0.65, 1.0)

    draw_sphere(1.0)


def render_orbiting_camera(angle: float) -> None:

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    glRotatef(-angle, 0.0, 1.0, 0.0)

    glTranslatef(0.0, 0.0, -CAM_DISTANCE)

    if USE_LIGHTING:
        setup_basic_lighting()

    glColor3f(1.0, 0.55, 0.35)

    draw_sphere(1.0)


def render_with_lookat(angle: float) -> None:

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    a = math.radians(angle)

    cam_x = ORBIT_RADIUS * math.sin(a)
    cam_z = ORBIT_RADIUS * math.cos(a)

    gluLookAt(
        cam_x,
        0.0,
        cam_z,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0
    )

    if USE_LIGHTING:
        setup_basic_lighting()

    glColor3f(0.95, 0.85, 0.35)

    draw_sphere(1.0)


def main() -> None:

    if not glfw.init():

        print("Error: no se pudo inicializar GLFW", file=sys.stderr)

        sys.exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)

    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    window = glfw.create_window(
        800,
        600,
        WINDOW_TITLE,
        None,
        None
    )

    if not window:

        glfw.terminate()

        print(
            "Error: no se pudo crear la ventana OpenGL",
            file=sys.stderr
        )

        sys.exit(1)

    glfw.make_context_current(window)

    glfw.swap_interval(1)

    mode = INITIAL_MODE

    def on_key(win, key, scancode, action, mods):

        nonlocal mode

        if action != glfw.PRESS:
            return

        if key in (glfw.KEY_ESCAPE, glfw.KEY_Q):

            glfw.set_window_should_close(win, True)

        elif key == glfw.KEY_1:

            mode = 1

        elif key == glfw.KEY_2:

            mode = 2

        elif key == glfw.KEY_3:

            mode = 3

    glfw.set_key_callback(window, on_key)

    glEnable(GL_DEPTH_TEST)

    glClearColor(0.08, 0.08, 0.12, 1.0)

    angle = 0.0

    while not glfw.window_should_close(window):

        fb_w, fb_h = glfw.get_framebuffer_size(window)

        if fb_h <= 0:
            fb_h = 1

        glViewport(0, 0, fb_w, fb_h)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

        gluPerspective(
            50.0,
            fb_w / float(fb_h),
            0.1,
            100.0
        )

        if not USE_LIGHTING:

            glDisable(GL_LIGHTING)

        if mode == 1:

            render_rotating_object(angle)

        elif mode == 2:

            render_orbiting_camera(angle)

        elif mode == 3:

            render_with_lookat(angle)

        angle += ANGLE_SPEED

        if angle >= 360.0:

            angle -= 360.0

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":

    main()

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
> gluLookAt() hace que la cámara sea más fácil de entender y mantener porque describe directamente la posición del ojo, el punto al que mira y el vector arriba.

4. **Luces:** Si la luz se define en el frame de la cámara sin reubicarla al mundo, ¿qué artefacto visual esperas al rotar solo el objeto?
> La luz parecerá pegada a la cámara en lugar de permanecer fija en el mundo.