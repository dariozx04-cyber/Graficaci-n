## Actividad casa

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
    gluPerspective(60, 800/600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():

    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)

   
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)


    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

 
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)


    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)


    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)

    
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)

    
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(0, 2, 0)

  
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)
    glEnd()

def draw_door():
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0.0)
    glVertex3f(-0.25, 0, 1.01)
    glVertex3f(0.25, 0, 1.01)
    glVertex3f(0.25, 0.6, 1.01)
    glVertex3f(-0.25, 0.6, 1.01)
    glEnd()

def draw_windows():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.7, 1.0)

   
    glVertex3f(-0.8, 0.5, 1.01)
    glVertex3f(-0.4, 0.5, 1.01)
    glVertex3f(-0.4, 0.8, 1.01)
    glVertex3f(-0.8, 0.8, 1.01)

    glVertex3f(0.4, 0.5, 1.01)
    glVertex3f(0.8, 0.5, 1.01)
    glVertex3f(0.8, 0.8, 1.01)
    glVertex3f(0.4, 0.8, 1.01)

    glEnd()

def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.7, 0.3)

    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)
    glEnd()

def draw_one_house(x, z):
    glPushMatrix()
    glTranslatef(x, 0, z)

    draw_cube()
    draw_roof()
    draw_door()
    draw_windows()

    glPopMatrix()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(8, 6, 12,
              0, 0, 0,
              0, 1, 0)

    draw_ground()

  
    draw_one_house(0, 0)
    draw_one_house(4, 0)
    draw_one_house(-4, 0)
    draw_one_house(0, -5)
    draw_one_house(4, -5)
    draw_one_house(-4, -5)

    glfw.swap_buffers(window)

def main():
    global window

    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Varias Casas 3D", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()