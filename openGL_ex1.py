from OpenGL.GL import *
from OpenGL.GLUT import *
def Model():
    pass

def View():
    pass

def Perspective():
    pass

def screen():
    pass

def draw():
    pass

def main():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    window = glutCreateWindow("OpenGl- Ex1")
    glutDisplayFunc( draw )
    glutMainLoop()

if __name__ == "__main__":
    main()