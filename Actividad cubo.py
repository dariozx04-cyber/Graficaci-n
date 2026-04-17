import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

window = None

a1 = 0   
a2 = 0
a3 = 0   
a4 = 0   

def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)

    glMatrixMode(GL_MODELVIEW)

def cubo():
    glBegin(GL_QUADS)


    glColor3f(1,0,0)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)

    
    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(1,-1,-1)

    
    glColor3f(0,0,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,1,-1)

   
    glColor3f(1,1,0)
    glVertex3f(1,-1,-1)
    glVertex3f(1,1,-1)
    glVertex3f(1,1,1)
    glVertex3f(1,-1,1)

  
    glColor3f(1,0,1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(1,1,1)
    glVertex3f(1,1,-1)


    glColor3f(0,1,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(1,-1,-1)
    glVertex3f(1,-1,1)
    glVertex3f(-1,-1,1)

    glEnd()

def draw():
    global a1, a2, a3, a4

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    glLoadIdentity()
    glTranslatef(-3, 2, -12)
    glRotatef(a1, 1, 0, 0)
    cubo()

  
    glLoadIdentity()
    glTranslatef(3, 2, -12)
    glRotatef(a2, 0, 1, 0)
    cubo()

   
    glLoadIdentity()
    glTranslatef(-3, -2, -12)
    glRotatef(a3, 0, 0, 1)
    cubo()


    glLoadIdentity()
    glTranslatef(3, -2, -12)
    glRotatef(a4, 1, 0, 0)
    glRotatef(a4, 0, 1, 0)
    glRotatef(a4, 0, 0, 1)
    cubo()

    glfw.swap_buffers(window)

    a1 += 0.1
    a2 += 0.1
    a3 += 0.1
    a4 += 0.1

def main():
    global window

    if not glfw.init():
        sys.exit()

    window = glfw.create_window(700, 700, "4 Cubos Rotando", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, 700, 700)

    init()

    while not glfw.window_should_close(window):
        draw()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()