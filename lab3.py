from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys
import numpy

name = b'ball_glut'
x_camera, y_camera, z_camera = 0, -20, 50
x_light, y_light, z_light = 0.0, 20.0, 4.0
camera_angle = (3 * pi) / 2
light_angle = 0
camera_angle_speed = 0.05
light_angle_speed = 0.0005
mas = []
stop_animation = False

matrix_model = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(name)
    glEnable(GL_DEPTH_TEST)


def init_camera():
    """ Задаем начальное положение камеры """
    gluLookAt(x_camera, y_camera, z_camera,
              0, 0, 0,
              0, 1, 0)


def init_light():
    """ Инициализируем источник света """
    ambientLight = [0.0, 0.0, 0.0, 1.0]
    diffuseLight = [1.0, 1.0, 1.0, 1.0]
    positionLight = [0.0, 0.0, 100.0, 1.0]
    specularLight = [1.0, 1.0, 1.0, 1.0]
    black = [0.0, 0.0, 0.0, 1.0]
    glEnable(GL_LIGHTING)
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, black)
    glEnable(GL_LIGHT0)
    #glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, True)

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight)
    glLightfv(GL_LIGHT0, GL_POSITION, positionLight)

    # gray = [1.0, 1.0, 1.0, 1]
    # glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, gray)
    #
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specularLight)
    glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, 128)


def special_keyboard_fun(button, x1, y1):
    global stop_animation

    if button == GLUT_KEY_RIGHT:
        my_translate(5, 0, 0)
    if button == GLUT_KEY_UP:
        my_translate(0, 5, 0)
    if button == GLUT_KEY_LEFT:
        my_translate(-5, 0, 0)
    if button == GLUT_KEY_DOWN:
        my_translate(0, -5, 0)

    if button == GLUT_KEY_F1:
        glutIdleFunc(None)
        stop_animation = True

    glutPostRedisplay()


def keyboardFun(button, x1, y1):
    if button == b'-':
        my_scale(0.5, 1, 1)
    if button == b'+':
        my_scale(2, 1, 1)

    if button == b'r':
        my_rotate(pi/2)

    if button == b't':
        my_rotate(-pi/2)

    glutPostRedisplay()


def func(mas):
    """ Вычисляем значения функции для построения графика """
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
    glPopMatrix()

    glEndList()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glCallList(1)
    glPushMatrix()
    glTranslate(0, 15, 0)
    glCallList(1)
    glPopMatrix()

    glutSwapBuffers()
    return


def set_camera_and_light():
    """ Установить камеру и источник света.
    Используется после изменений некоторых параметров,
    например, когда изменились координаты источника света
    """
    global x_light, y_light, z_light, light_angle
    global x_camera, y_camera, z_camera, camera_angle

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x_camera, y_camera, z_camera, 0, 0, 0, 0, 1, 0)

    positionLight = [x_light, y_light, z_light, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, positionLight)


def idf():
    """ Функция, которая вызывается когда ничего ен происходит
    т. е. не прорисовывается ничего, не нажимаются клавиши и т. п.
    """
    global x_light, y_light, z_light, light_angle
    light_angle += light_angle_speed
    x_light = 20 * cos(light_angle)
    y_light = 20 * sin(light_angle)

    set_camera_and_light()
    glutPostRedisplay()


def timf(value):
    """ Функция, которая вызывается с некоторым периодом """
    global x_camera, y_camera, z_camera, camera_angle
    camera_angle += camera_angle_speed
    x_camera = 20 * cos(camera_angle)
    y_camera = 20 * sin(camera_angle)

    set_camera_and_light()
    glutPostRedisplay()

    if stop_animation:
        return glutTimerFunc(20, timf, 0)


def read_matrix():
    """ Считать текущее значение матрици """
    global matrix_model
    proxy_list = (GLfloat * 16)()
    glGetFloatv(GL_MODELVIEW_MATRIX, proxy_list)
    proxy_list = list(proxy_list)

    iterator = -1
    for i in range(0, len(proxy_list), 4):
        iterator += 1
        for j in range(0, 4):
            matrix_model[iterator][j] = proxy_list[i + j]


def my_translate(x, y, z):
    """ Моя собственная функция переноса """
    global matrix_model
    mas1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]]
    read_matrix()
    matrix_model = numpy.dot(matrix_model, mas1)

    print("MODELVIEW MATRIX AFTER TRANSLATING: ")
    print(matrix_model)
    glLoadMatrixf(matrix_model)


def my_scale(x, y, z):
    """ Моя собственная функция изменения масштаба """
    global matrix_model
    read_matrix()
    mas1 = [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    matrix_model = numpy.dot(matrix_model, mas1)

    print("MODELVIEW MATRIX AFTER SCALING: ")
    print(matrix_model)
    glLoadMatrixf(matrix_model)


def my_rotate(angle):
    """ Моя собственная функция поворота """
    global matrix_model
    mas1 = [[cos(angle), sin(angle), 0, 0], [-sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0], [0, 0, 0, 1]]
    read_matrix()
    matrix_model = numpy.dot(matrix_model, mas1)

    print("MODELVIEW MATRIX AFTER ROTATING: ")
    print(matrix_model)
    glLoadMatrixf(matrix_model)


def main():
    init()

    glClearColor(0, 0, 0, 1)

    glutDisplayFunc(display)
    glutIdleFunc(idf)
    glutTimerFunc(40, timf, 0)
    glutKeyboardFunc(keyboardFun)
    glutSpecialFunc(special_keyboard_fun)

    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40, 1, 1, 400)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    init_camera()
    init_light()

    func(mas)
    list_of_commands()

    glutMainLoop()
    return

main()