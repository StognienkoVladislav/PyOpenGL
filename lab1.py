from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

"""
    trianglesList includes triangles
    quadranglesList includes quadrangle
"""
trianglesList = []
quadranglesList = []


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3ub(0, 180, 0)
        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)
        glEnd()

        self.drawTriangleLine()

    def drawTriangleLine(self):
        """
            Draw triangle border
        """
        glBegin(GL_LINES)
        glColor3ub(0, 0, 0)

        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)

        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)

        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point1.x, self.point1.y)
        glEnd()


class Quadrangle:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def draw(self):
        glBegin(GL_POLYGON)
        glColor3ub(0, 180, 0)
        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point4.x, self.point4.y)
        glEnd()

        self.drawQuadrangleLine()

    def drawQuadrangleLine(self):
        """
            Draw polygon border
        """
        glBegin(GL_LINES)
        glColor3ub(0, 0, 0)

        glVertex2d(self.point1.x, self.point1.y)
        glVertex2d(self.point2.x, self.point2.y)

        glVertex2d(self.point2.x, self.point2.y)
        glVertex2d(self.point3.x, self.point3.y)

        glVertex2d(self.point3.x, self.point3.y)
        glVertex2d(self.point4.x, self.point4.y)

        glVertex2d(self.point4.x, self.point4.y)
        glVertex2d(self.point1.x, self.point1.y)
        glEnd()

def initFigure():
    """
        Init Figure witch consists of triangles (tr) and polygons (quard) and
        then we add triangles and polygons to lists
    """
    #tr1 = Triangle(Point(0.0, 0.0), Point(2.0, 2.0), Point(2.0, 0.0))
    #trianglesList.append(tr1)

    tr1 = Triangle(Point(0.0, 0.0), Point(1.0, 1.0), Point(-1.0, 1.0))
    trianglesList.append(tr1)

    tr2 = Triangle(Point(-1.0, 1.0), Point(0.0, 0.0), Point(-1.0, -1.0))
    trianglesList.append(tr2)

    quard1 = Quadrangle(Point(tr2.point2.x, tr2.point2.y), Point(tr2.point3.x, tr2.point3.y),
                        Point(tr2.point3.x, tr2.point3.y - 1 - sqrt(1)),
                        Point(tr2.point2.x, tr2.point2.y - 1 - sqrt(1)))
    quadranglesList.append(quard1)

    quard2 = Quadrangle(Point(quard1.point2.x , quard1.point2.y - 0.4),
                        Point(quard1.point2.x - 1, quard1.point2.y + 0.8),
                        Point(quard1.point2.x - 1 - sqrt(1), quard1.point2.y - 0.4),
                        Point(quard1.point2.x - 1, quard1.point2.y - 1.4))
    quadranglesList.append(quard2)

    tr3 = Triangle(Point(quard2.point1.x, quard2.point1.y),
                   Point(quard2.point3.x, quard2.point3.y - (abs(quard2.point2.y - quard2.point4.y))),
                   Point(quard2.point1.x, quard2.point3.y - 2*(abs(quard1.point2.y - quard1.point3.y))))
    trianglesList.append(tr3)

    tr4 = Triangle(Point(quard2.point4.x, quard2.point4.y),
                   Point(quard2.point3.x - 0.3, quard2.point3.y + 0.3),
                   Point(quard2.point4.x - 0.3 - sqrt(5), quard2.point4.y))
    trianglesList.append(tr4)

    tr5 = Triangle(Point(tr4.point1.x, tr4.point1.y),
                   Point(tr4.point3.x, tr4.point3.y),
                   Point(tr4.point3.x, tr3.point3.y))
    trianglesList.append(tr5)


def initFun():
    glLoadIdentity()
    gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
    glLineWidth(3)
    initFigure()


def displayFun():

    glClearColor(255, 108, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    for figure in range(len(trianglesList)):
        trianglesList[figure].draw()

    for figure in range(len(quadranglesList)):
        quadranglesList[figure].draw()

    glFlush()


def specialKeyboardFun(button, x, y):
    """
        Translate figure
    """
    if button == GLUT_KEY_LEFT:
        glTranslate(-1, 0, 0)
    if button == GLUT_KEY_RIGHT:
        glTranslate(1, 0, 0)
    if button == GLUT_KEY_UP:
        glTranslate(0, 1, 0)
    if button == GLUT_KEY_DOWN:
        glTranslate(0, -1, 0)

    displayFun()

def keyboardFun(button):
    if button == b'-':
        glScale(1, 0.5, 0)

    if button == b'+':
        glScale(1, 2, 0)

    """
        Rotate figure
    """
    if button == b'r':
        glRotate(90, 0, 0, 1)

    if button == b't':
        glRotate(-90, 0, 0, 1)

    displayFun()


glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Polyline")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(displayFun)
glutKeyboardFunc(keyboardFun)
glutSpecialFunc(specialKeyboardFun)
initFun()
glutMainLoop()