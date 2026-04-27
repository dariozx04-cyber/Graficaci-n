## Actividad de camara

Dario Padilla Moreno

Codigo:

import glfw

from OpenGL.GL import *

from OpenGL.GLU import gluPerspective, gluLookAt

import sys

window = None

def init():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 800/600, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():

    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)

    # Frente
    glVertex3f(-1,0,1)
    glVertex3f(1,0,1)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)

    # Atrás
    glVertex3f(-1,0,-1)
    glVertex3f(1,0,-1)
    glVertex3f(1,1,-1)
    glVertex3f(-1,1,-1)

    # Izquierda
    glVertex3f(-1,0,-1)
    glVertex3f(-1,0,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,1,-1)

    # Derecha
    glVertex3f(1,0,-1)
    glVertex3f(1,0,1)
    glVertex3f(1,1,1)
    glVertex3f(1,1,-1)

    # Arriba
    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)

    # Abajo
    glVertex3f(-1,0,-1)
    glVertex3f(1,0,-1)
    glVertex3f(1,0,1)
    glVertex3f(-1,0,1)
    glEnd()

def draw_roof():

    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)

    glVertex3f(-1,1,1)
    glVertex3f(1,1,1)
    glVertex3f(0,2,0)

    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(0,2,0)

    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(0,2,0)

    glVertex3f(1,1,-1)
    glVertex3f(1,1,1)
    glVertex3f(0,2,0)
    glEnd()

def draw_door():

    glBegin(GL_QUADS)
    glColor3f(0.4,0.2,0)

    glVertex3f(-0.3,0,1.01)
    glVertex3f(0.3,0,1.01)
    glVertex3f(0.3,0.6,1.01)
    glVertex3f(-0.3,0.6,1.01)
    glEnd()

def draw_windows():

    glBegin(GL_QUADS)
    glColor3f(0.2,0.7,1)

    # izquierda
    glVertex3f(-0.8,0.5,1.01)
    glVertex3f(-0.4,0.5,1.01)
    glVertex3f(-0.4,0.8,1.01)
    glVertex3f(-0.8,0.8,1.01)

    # derecha
    glVertex3f(0.4,0.5,1.01)
    glVertex3f(0.8,0.5,1.01)
    glVertex3f(0.8,0.8,1.01)
    glVertex3f(0.4,0.8,1.01)
    glEnd()

def draw_ground():

    glBegin(GL_QUADS)
    glColor3f(0.2,0.8,0.2)

    glVertex3f(-20,0,20)
    glVertex3f(20,0,20)
    glVertex3f(20,0,-20)
    glVertex3f(-20,0,-20)
    glEnd()

def house(x,z):

    glPushMatrix()
    glTranslatef(x,0,z)

    draw_cube()
    draw_roof()
    draw_door()
    draw_windows()

    glPopMatrix()

def draw_scene():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    
    gluLookAt(
       4,3,8,   
        2,4,2,     
        0,10,10 )

    draw_ground()

    house(0,0)
    house(4,0)
    house(-4,0)
    house(0,-5)
    house(4,-5)
    house(-4,-5)

    glfw.swap_buffers(window)

def main():

    global window

    if not glfw.init():
        sys.exit()

    window = glfw.create_window(800,600,"Casas con gluLookAt",None,None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":

    main()