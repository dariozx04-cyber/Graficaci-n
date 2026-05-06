# ACTIVIDAD Iluminacion

Dario Padilla Moreno

Codigo:
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

rotation = 0.0

def draw_sphere(radius, slices=30, stacks=30):

    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)  # normales suaves
    gluSphere(quad, radius, slices, stacks)
    gluDeleteQuadric(quad)

def set_material(ambient, diffuse, specular, shininess):

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

def draw_eye():

    glPushMatrix()

   
    set_material(
        [0.85, 0.67, 0.65, 1.0],
        [0.85, 0.67, 0.65, 1.0],
        [0.2, 0.2, 0.2, 1.0],
        10
    )
    glPushMatrix()
    glTranslatef(0.7, 0, 0)
    draw_sphere(0.54)
    glPopMatrix()

   
    set_material(
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0.8, 0.8, 0.8, 1],
        50
    )
    glPushMatrix()
    glTranslatef(0.56, 0, 0)
    draw_sphere(0.6)
    glPopMatrix()

   
    set_material(
        [0.2, 0.3, 0.6, 1],
        [0.4, 0.5, 0.9, 1],
        [0.6, 0.6, 0.6, 1],
        30
    )
    glPushMatrix()
    glTranslatef(0.49, 0, 0)
    draw_sphere(0.55)
    glPopMatrix()

    
    set_material(
        [0, 0, 0, 1],
        [0.1, 0.1, 0.1, 1],
        [0.9, 0.9, 0.9, 1],
        100
    )
    glPushMatrix()
    glTranslatef(0.3, 0, 0)
    draw_sphere(0.4)
    glPopMatrix()

    glPopMatrix()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

 
    light_position = [2.0, 2.0, 2.0, 1.0]

    # Componentes de la luz
    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [0.8, 0.8, 0.8, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def main():

    global rotation

    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Ojo con Iluminación", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.54, 0.72, 0.84, 1.0)
    setup_lighting()

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800/600, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)

        rotation += 0.5
        glRotatef(rotation, 0, 1, 0)

        draw_eye()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":

    main()