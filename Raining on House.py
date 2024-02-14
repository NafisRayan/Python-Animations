import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

raindrop_count = 1000
rain_speed = 0.01
rain_angle = 0.0
house_color = [1.0, 0.5, 0.31]
day_night_cycle = 0.0
color_step = 0.01  # initialize color_step variable

def draw_raindrops():
    glColor3f(0.0, 0.0, 1.0)

    for i in range(raindrop_count):
        glPushMatrix()
        glTranslatef(raindrops[i][0], raindrops[i][1], 0)
        glRotatef(rain_angle, 0.0, 0.0, 1.0)

        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(0, -0.1)  # Adjust the length by changing the y-coordinate
        glEnd()

        glBegin(GL_POINTS)
        glVertex2f(0, -0.1)  # Adjust the length by changing the y-coordinate
        glEnd()

        glPopMatrix()

def draw_house():
    glColor3fv(house_color)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    glColor3f(0.7, 0.2, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.0, 1.0)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.5)
    glVertex2f(-0.2, 0.0)
    glVertex2f(0.2, 0.0)
    glVertex2f(0.2, -0.5)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.3, 0.2)
    glVertex2f(-0.3, 0.4)
    glVertex2f(-0.1, 0.4)
    glVertex2f(-0.1, 0.2)
    glEnd()

def update():
    global raindrop_count, rain_angle, house_color, day_night_cycle, color_step

    for i in range(raindrop_count):
        raindrops[i][1] -= rain_speed

        if raindrops[i][1] < -1.0:
            raindrops[i][1] = 1.0 + random.uniform(0.0, 0.1)
            raindrops[i][0] = random.uniform(-0.8, 0.8)

    rain_angle += 0.01
    if rain_angle > 10.0 or rain_angle < -10.0:
        rain_angle = 0.0

    day_night_cycle += color_step
    if day_night_cycle > 1.0 or day_night_cycle < 0.0:
        color_step = -color_step

    r = 1.0 - day_night_cycle
    g = day_night_cycle * 0.5
    b = day_night_cycle * 0.31
    house_color = [r, g, b]

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    draw_house()
    draw_raindrops()
    glFlush()

def idle():
    update()
    glutPostRedisplay()

def key_press(key, x, y):
    global rain_angle, color_step

    if key == b'Left':
        rain_angle -= 0.1
    elif key == b'Right':
        rain_angle += 0.1
    elif key == b'd':  # Change house color to dark
        color_step = 0.01
    elif key == b'l':  # Change house color to light
        color_step = -0.01

def main():
    global raindrops
    raindrops = [[random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)] for _ in range(raindrop_count)]

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"House Drawing")
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(key_press)
    glutMainLoop()

main()
