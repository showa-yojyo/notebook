#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""glsl-minimal.py

Reference:
  * rndblnch / opengl-programmable <bitbucket.org/rndblnch/opengl-programmable>
  * Simple Demo for GLSL <www.lighthouse3d.com>
"""
# pylint: disable=unused-argument
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_TITLE = b"Simple Demo for GLSL"
WINDOW_SX, WINDOW_SY = 320, 240
WINDOW_X, WINDOW_Y = 100, 100

# minimal.vert
VERT_SHADER_SOURCE = """
void main()
{
    gl_Position = ftransform();
}
"""

# minimal.frag
FRAG_SHADER_SOURCE = """
void main()
{
     gl_FragColor = vec4(1., 0.07843137, 0.57647059, 1.);
}
"""

class GLSLMinimal(object):
    """A minimal program which demonstrates GLSL."""

    def __init__(self):
        """Initialize an instance of class GLSLMinimal."""
        self.rotation = 0

    def run(self, args):
        """Run a program.

        Args:
          args: Command line parameters passed to glutInit.
        """
        self.init_glut(args)

        print("Vendor: {}\nRenderer: {}\nVersion: {}\nGLSL: {}".format(
            glGetString(GL_VENDOR).decode(),
            glGetString(GL_RENDERER).decode(),
            glGetString(GL_VERSION).decode(),
            glGetString(GL_SHADING_LANGUAGE_VERSION).decode()),
              file=sys.stderr, flush=True)

        self.init_program()
        self.init_opengl()
        return glutMainLoop()

    def init_glut(self, args):
        """Initialize the GLUT state.

        Args:
          args: Command line parameters passed to glutInit.
        """

        glutInit(args)
        glutInitDisplayMode(
            GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)

        glutInitWindowSize(WINDOW_SX, WINDOW_SY)
        glutInitWindowPosition(WINDOW_X, WINDOW_Y)
        glutCreateWindow(WINDOW_TITLE)

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)

    def init_program(self):
        """Setup shaders."""

        def create_shader(shader_type, source):
            """Compile a shader."""
            shader = glCreateShader(shader_type)
            glShaderSource(shader, source)
            glCompileShader(shader)
            if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
                raise RuntimeError(glGetShaderInfoLog(shader))
            return shader

        vert_shader = create_shader(GL_VERTEX_SHADER, VERT_SHADER_SOURCE)
        frag_shader = create_shader(GL_FRAGMENT_SHADER, FRAG_SHADER_SOURCE)

        program = glCreateProgram()
        glAttachShader(program, vert_shader)
        glAttachShader(program, frag_shader)

        glDeleteShader(vert_shader)
        glDeleteShader(frag_shader)

        glLinkProgram(program)
        if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(program))

        glUseProgram(program)

    def init_opengl(self):
        """Initialize the OpenGL state."""

        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glEnable(GL_CULL_FACE)

    def display(self):
        """The display callback function."""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(
            0.0, 0.0, 5.0,
            0.0, 0.0, -1.0,
            0.0, 1.0, 0.0)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, 0.5, 1, 0])
        glRotatef(self.rotation, 0, 1, 1)
        glutSolidTeapot(1)

        self.rotation += 0.1

        glutSwapBuffers()

    def reshape(self, width, height):
        """The reshape callback function.

        Args:
          width (int): the width of new window size in pixels.
          height (int): the width of new window size in pixels.
        """

        # Prevent a divide by zero, when window is too short.
        if height == 0:
            return

        # Reset the coordinate system before modifying.
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Set the viewport to be the entire window.
        glViewport(0, 0, width, height)

        # Set the correct perspective.
        gluPerspective(45, width / height, 1, 1000)
        glMatrixMode(GL_MODELVIEW)

    def keyboard(self, key, x, y):
        """The keyboard callback function.

        Args:
          key (?): n The ASCII character that the user typed into the window.
          x (int): X coordinate of the mouse location in window relative
            coordinates when the key was pressed.
          y (int): Y coordinate of the mouse location in window relative
            coordinates when the key was pressed.
        """

        if ord(key) == 0o33 or key == b'q':
            print('Exit program.', file=sys.stderr, flush=True)
            sys.exit(0)

def main(args):
    """The main function.

    Args:
        args: Command line parameters passed to glutInit.
    """
    app = GLSLMinimal()
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
