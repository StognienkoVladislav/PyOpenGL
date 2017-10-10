from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys

name = b'ball_glut'
x, y, z = 0, 0, 40
angle_XY = 0
angle_YZ = 0
lx, ly, lz = 0, 0, 0

mas = []


def special_keyboard_fun(button, x1, y1):
    global x, y, z, lx, ly, lz, angle_XY, angle_YZ

    if button == GLUT_KEY_UP:
        angle_XY += 0.05
        if z > 0:
            ly = sin(angle_XY)
            lz = -cos(angle_XY)
        elif z < 0:
            ly = sin(angle_XY)
            lz = cos(angle_XY)

    if button == GLUT_KEY_DOWN:
        angle_XY -= 0.05
        if z > 0:
            ly = sin(angle_XY)
            lz = -cos(angle_XY)
        elif z < 0:
            ly = sin(angle_XY)
            lz = cos(angle_XY)
    if button == GLUT_KEY_RIGHT:
        angle_YZ += 0.05
        lx = sin(angle_YZ)
        lz = -cos(angle_YZ)
    if button == GLUT_KEY_LEFT:
        angle_YZ -= 0.05
        lx = sin(angle_YZ)
        lz = -cos(angle_YZ)

    glLoadIdentity()
    print(x, y, z, lx, ly, lz)
    gluLookAt(x, y, z, x + lx, y + ly, z + lz, 0, 1, 0)
    glutPostRedisplay()


def keyboardFun(button, x1, y1):
    global x, y, z, lx, ly, lz
    if button == b'-':
        z += 5
    if button == b'+':
        z -= 5

    glLoadIdentity()
    print(x, y, z, lx, ly, lz)
    gluLookAt(x, y, z, x + lx, y + ly, z + lz, 0, 1, 0)

    if button == b'q':
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-40.0, 40.0, -30.0, 30.0, 1, 40)
        glMatrixMode(GL_MODELVIEW)

    if button == b'w':
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40, 1, 1, 400)
        glMatrixMode(GL_MODELVIEW)

    if button == b'e':
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-tan(0.349066), tan(0.349066), -tan(0.349066), tan(0.349066), 1, 400)
        #glFrustum(-1, 1, -1, 1, 1, 400)
        #gluPerspective(40, 1, 1, 400)
        glMatrixMode(GL_MODELVIEW)

    glutPostRedisplay()


def func(mas):
    for i in range(10):
        for j in range(10):
            mas.append(i)
            mas.append(j)
            mas.append(sqrt(i * j))

            mas.append(i + 1)
            mas.append(j)
            mas.append(sqrt((i + 1) * j))

            mas.append(i + 1)
            mas.append(j + 1)
            mas.append(sqrt((i + 1) * (j + 1)))

            mas.append(i)
            mas.append(j + 1)
            mas.append(sqrt(i * (j + 1)))

    return mas


def list_of_commands():
    glNewList(1, GL_COMPILE)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glPushMatrix()
    glColor3ub(255, 0, 0)
    glutSolidSphere(5, 50, 10)
    glTranslate(10, 0, 0)
    glutWireSphere(5, 50, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3ub(255, 0, 0)
    glTranslate(-10, 0, 0)
    glutSolidCube(5)
    glutWireCube(10)
    glPopMatrix()

    glPushMatrix()
    glTranslate(20, 0, 0)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_DOUBLE, 0, mas)

    glColor3ub(255, 140, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glDrawArrays(GL_QUADS, 0, 400)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3ub(255, 0, 0)
    glDrawArrays(GL_QUADS, 0, 400)
    glPopMatrix()

    glEndList()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glCallList(1)

    glPushMatrix()
    glTranslate(0, -10, 0)
    glCallList(1)
    glPopMatrix()

    glutSwapBuffers()
    return


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(name)

    glClearColor(0, 0, 0, 1)
    glShadeModel(GL_SMOOTH)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboardFun)
    glutSpecialFunc(special_keyboard_fun)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40, 1, 1, 400)
    glMatrixMode(GL_MODELVIEW)
    #glEnable(GL_DEPTH_TEST)
    gluLookAt(x, y, z,
              0, 0, 0,
              0, 1, 0)
    func(mas)
    list_of_commands()
    glutMainLoop()
    return


main()