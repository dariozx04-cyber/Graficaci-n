# Proyecto 3
Dario Padilla Moreno

## Objetivo
Crear un pueblo en realidad aumentada atraves de una marca.

## Codigo:
from __future__ import annotations

import sys

import cv2

import glfw

import numpy as np

import math

import time

from OpenGL.GL import *

from OpenGL.GLU import (
    GLU_FILL,
    gluNewQuadric,
    gluQuadricDrawStyle,
    gluSphere,
    gluCylinder,
)

CAMERA_INDEX = 0

MARKER_LENGTH_M = 0.10

ARUCO_DICT = cv2.aruco.DICT_4X4_50

MARKER_ID = 0

MODEL_SCALE = 0.05

WINDOW_TITLE = "Pueblo Vivo - Pantalla y Brillo Ajustados"

ZNear, ZFar = 0.01, 100.0

def draw_cube(size=1.0, height_scale=1.0):

    s = size / 2.0
    h = size * height_scale
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1); glVertex3f(-s, 0, s); glVertex3f(s, 0, s); glVertex3f(s, h, s); glVertex3f(-s, h, s)
    glNormal3f(0, 0, -1); glVertex3f(-s, 0, -s); glVertex3f(-s, h, -s); glVertex3f(s, h, -s); glVertex3f(s, 0, -s)
    glNormal3f(0, 1, 0); glVertex3f(-s, h, s); glVertex3f(s, h, s); glVertex3f(s, h, -s); glVertex3f(-s, h, -s)
    glNormal3f(-1, 0, 0); glVertex3f(-s, 0, -s); glVertex3f(-s, 0, s); glVertex3f(-s, h, s); glVertex3f(-s, h, -s)
    glNormal3f(1, 0, 0); glVertex3f(s, 0, -s); glVertex3f(s, h, -s); glVertex3f(s, h, s); glVertex3f(s, 0, s)
    glEnd()

def draw_person(t, orbit_radius, scale):

    angle = t * 2.0 
    x = math.cos(angle) * orbit_radius
    z = math.sin(angle) * orbit_radius
    
    glPushMatrix()
    glTranslatef(x, 0, z) # Base alineada al piso
    glColor3f(0.0, 0.0, 1.0) 
    q = gluNewQuadric()
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluCylinder(q, scale * 0.1, scale * 0.1, scale * 0.5, 10, 10)
    glPopMatrix()
    glTranslatef(0, scale * 0.6, 0)
    glColor3f(1.0, 0.8, 0.6)
    gluSphere(q, scale * 0.15, 10, 10)
    glPopMatrix()

def draw_lamp_post(scale):

    glColor3f(0.3, 0.3, 0.3)
    glPushMatrix()
    glScalef(0.1, 2.0, 0.1)
    draw_cube(scale)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, scale * 1.0, 0)
    glColor3f(1.0, 1.0, 0.5)
    q = gluNewQuadric()
    gluSphere(q, scale * 0.2, 10, 10)
    glPopMatrix()

def draw_tree(scale):

    glColor3f(0.4, 0.2, 0.1)
    glPushMatrix()
    glScalef(0.2, 1.0, 0.2)
    draw_cube(scale)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, scale * 0.7, 0)
    glColor3f(0.1, 0.6, 0.1)
    q = gluNewQuadric()
    gluSphere(q, scale * 0.6, 10, 10)
    glPopMatrix()

def draw_bush(scale):

    glColor3f(0.0, 0.4, 0.0)
    q = gluNewQuadric()
    gluSphere(q, scale * 0.3, 10, 10)

def draw_helicopter(scale, t, offset_angle, radius, height, color):

    glPushMatrix()
    angle = t + offset_angle
    curr_x = math.cos(angle) * radius
    curr_z = math.sin(angle) * radius
    glTranslatef(curr_x, height, curr_z)
    glRotatef(math.degrees(-angle), 0, 1, 0)
    glColor3f(*color)
    q = gluNewQuadric()
    gluSphere(q, scale, 10, 10)
    glPushMatrix()
    glTranslatef(0, 0, -scale)
    glScalef(0.3, 0.3, 1.5)
    draw_cube(scale)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, scale * 0.8, 0)
    glRotatef(t * 1000, 0, 1, 0)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_LINES)
    glVertex3f(-scale*2, 0, 0); glVertex3f(scale*2, 0, 0)
    glVertex3f(0, 0, -scale*2); glVertex3f(0, 0, scale*2)
    glEnd()
    glPopMatrix()
    glPopMatrix()

def draw_house(x, z, scale, color):

    glPushMatrix()
    glTranslatef(x, 0, z)
    glColor3f(*color)
    draw_cube(scale)
    s = scale / 2.0
    glColor3f(0.3, 0.15, 0.05)
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    glVertex3f(-scale*0.15, 0, s+0.001); glVertex3f(scale*0.15, 0, s+0.001)
    glVertex3f(scale*0.15, scale*0.4, s+0.001); glVertex3f(-scale*0.15, scale*0.4, s+0.001)
    glEnd()
    glColor3f(0.6, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    ts = s + 0.02; th = scale * 1.5
    glNormal3f(-0.5, 0.7, 0.5); glVertex3f(0, th, 0); glVertex3f(-ts, scale, ts); glVertex3f(ts, scale, ts)
    glNormal3f(0.5, 0.7, 0.5); glVertex3f(0, th, 0); glVertex3f(ts, scale, ts); glVertex3f(ts, scale, -ts)
    glNormal3f(0.5, 0.7, -0.5); glVertex3f(0, th, 0); glVertex3f(ts, scale, -ts); glVertex3f(-ts, scale, -ts)
    glNormal3f(-0.5, 0.7, -0.5); glVertex3f(0, th, 0); glVertex3f(-ts, scale, -ts); glVertex3f(-ts, scale, ts)
    glEnd()
    glPopMatrix()

def draw_big_building(x, z, scale):

    glPushMatrix()
    glTranslatef(x, 0, z)
    glColor3f(0.5, 0.5, 0.5)
    draw_cube(scale, height_scale=3.5)
    s = scale / 2.0
    glColor3f(1.0, 0.9, 0.2)
    for floor in range(1, 7):
        y = floor * scale * 0.5
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glVertex3f(-s*0.5, y, s+0.001); glVertex3f(s*0.5, y, s+0.001)
        glVertex3f(s*0.5, y+0.01, s+0.001); glVertex3f(-s*0.5, y+0.01, s+0.001)
        glEnd()
    glPopMatrix()

def draw_village(base_scale):

    t = time.time()
    glDisable(GL_LIGHTING)
    glColor3f(0.2, 0.4, 0.2)
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glVertex3f(-base_scale*7, 0, -base_scale*7); glVertex3f(base_scale*7, 0, -base_scale*7)
    glVertex3f(base_scale*7, 0, base_scale*7); glVertex3f(-base_scale*7, 0, base_scale*7)
    glEnd()
    
    glColor3f(0.3, 0.2, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-base_scale*7, 0.001, -base_scale*0.5); glVertex3f(base_scale*7, 0.001, -base_scale*0.5)
    glVertex3f(base_scale*7, 0.001, base_scale*0.5); glVertex3f(-base_scale*7, 0.001, base_scale*0.5)
    glVertex3f(-base_scale*0.5, 0.001, -base_scale*7); glVertex3f(base_scale*0.5, 0.001, -base_scale*7)
    glVertex3f(base_scale*0.5, 0.001, base_scale*7); glVertex3f(-base_scale*0.5, 0.001, base_scale*7)
    glEnd()
    glEnable(GL_LIGHTING)

    draw_big_building(0, 0, base_scale)
    
    num_elements = 8
    radius = base_scale * 3.5
    for i in range(num_elements):
        angle = i * (2 * math.pi / num_elements)
        x = math.cos(angle) * radius
        z = math.sin(angle) * radius
        
        draw_house(x, z, base_scale*0.8, (0.9, 0.9, 0.8))
        
        glPushMatrix()
        glTranslatef(x + base_scale, 0, z + base_scale)
        if i % 3 == 0: draw_tree(base_scale)
        elif i % 3 == 1: draw_lamp_post(base_scale * 0.4)
        else: draw_bush(base_scale)
        glPopMatrix()

    draw_person(t, base_scale * 2.0, base_scale)
    draw_person(t + 2.0, base_scale * 2.5, base_scale)

    draw_helicopter(base_scale*0.3, t, 0, base_scale*4, base_scale*3, (0, 0, 1))
    draw_helicopter(base_scale*0.3, -t * 0.8, math.pi, base_scale*6, base_scale*5, (1, 0, 0))

def modelview_from_pose(rvec, tvec):

    R, _ = cv2.Rodrigues(rvec)
    M = np.eye(4)
    M[:3, :3] = R
    M[:3, 3] = tvec.flatten()
    M = np.diag([1.0, -1.0, -1.0, 1.0]) @ M
    rot_x_90 = np.eye(4)
    angle = np.radians(90)
    rot_x_90[1, 1], rot_x_90[1, 2] = np.cos(angle), -np.sin(angle)
    rot_x_90[2, 1], rot_x_90[2, 2] = np.sin(angle), np.cos(angle)
    M = M @ rot_x_90
    return M.T.astype(np.float32)

def projection_from_k(width, height):

    f = float(max(width, height))
    P = np.zeros((4, 4), dtype=np.float32)
    P[0, 0], P[1, 1] = 2.0 * f / width, 2.0 * f / height
    P[2, 2], P[2, 3] = -(ZFar + ZNear) / (ZFar - ZNear), -1.0
    P[3, 2] = -2.0 * ZFar * ZNear / (ZFar - ZNear)
    return P

def main():

    global MODEL_SCALE
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    if not cap.isOpened(): return
    ret, probe = cap.read()
    h_orig, w_orig = probe.shape[:2]
    w, h = int(w_orig * 1.5), int(h_orig * 1.5)
    
    if not glfw.init(): return
    window = glfw.create_window(w, h, WINDOW_TITLE, None, None)
    glfw.make_context_current(window)

    def on_key(win, key, sc, action, mods):

        global MODEL_SCALE
        if key == glfw.KEY_ESCAPE: glfw.set_window_should_close(win, True)
        if key in (glfw.KEY_EQUAL, glfw.KEY_KP_ADD): MODEL_SCALE *= 1.1
        if key in (glfw.KEY_MINUS, glfw.KEY_KP_SUBTRACT): MODEL_SCALE /= 1.1
    glfw.set_key_callback(window, on_key)

    tex_id = glGenTextures(1)
    while not glfw.window_should_close(window):
        ret, frame = cap.read()
        if not ret: continue
        
        # Ajuste de brillo para el fondo
        bright_frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)
        
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION); glLoadIdentity(); glOrtho(0, w, 0, h, -1, 1)
        glMatrixMode(GL_MODELVIEW); glLoadIdentity()
        glDisable(GL_DEPTH_TEST); glDisable(GL_LIGHTING); glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        
        tex_data = cv2.flip(cv2.cvtColor(bright_frame, cv2.COLOR_BGR2RGB), 0)
        frame_resized = cv2.resize(tex_data, (w, h))
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, frame_resized)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glBegin(GL_QUADS)
        glTexCoord2f(0,0); glVertex2f(0,0); glTexCoord2f(1,0); glVertex2f(w,0)
        glTexCoord2f(1,1); glVertex2f(w,h); glTexCoord2f(0,1); glVertex2f(0,h)
        glEnd(); glDisable(GL_TEXTURE_2D)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detector = cv2.aruco.ArucoDetector(cv2.aruco.getPredefinedDictionary(ARUCO_DICT))
        corners, ids, _ = detector.detectMarkers(gray)
        if ids is not None and MARKER_ID in ids.flatten():
            idx = np.where(ids.flatten() == MARKER_ID)[0][0]
            obj_pts = np.array([[-1,1,0],[1,1,0],[1,-1,0],[-1,-1,0]], dtype=np.float32) * (MARKER_LENGTH_M/2)
            K = np.array([[w_orig, 0, w_orig/2], [0, w_orig, h_orig/2], [0, 0, 1]], dtype=np.float32)
            _, rvec, tvec = cv2.solvePnP(obj_pts, corners[idx], K, np.zeros(5))
            
            glEnable(GL_DEPTH_TEST); glClear(GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION); glLoadMatrixf(projection_from_k(w, h))
            glMatrixMode(GL_MODELVIEW); glLoadMatrixf(modelview_from_pose(rvec, tvec))
            
            # Iluminación clara y ambiental
            glEnable(GL_LIGHTING); glEnable(GL_LIGHT0); glEnable(GL_COLOR_MATERIAL)
            glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.6, 0.6, 0.6, 1.0])
            glLightfv(GL_LIGHT0, GL_POSITION, (0, 10, 5, 1))
            
            draw_village(MODEL_SCALE)

        glfw.swap_buffers(window)
        glfw.poll_events()
    cap.release(); glfw.terminate()

if __name__ == "__main__":

    main()

  ## Conclusion final
En este proyecto se aplica la vision artificial y el mundo real ya que se aplico el uso de un marcadorpara poder realizar el proyecto al igual que comandos de OpenCv y de OpenGL junto con comandos de integración matematica.

Se uilizo solvePnP para calcular la posición real del marcador y glLoadMatrixf para sincronizar esa posición con la cámara virtual de OpenGL.