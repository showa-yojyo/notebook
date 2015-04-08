#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""glappbase.py: Define class GLAppBase

Reference:
  * rndblnch / opengl-programmable <bitbucket.org/rndblnch/opengl-programmable>
  * Simple Demo for GLSL <www.lighthouse3d.com>
  * OpenGLBook.com <openglbook.com>
"""

# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

CONTEXT_VERSION = 3, 1
WINDOW_TITLE = b"PyOpenGL Demo"
WINDOW_SX, WINDOW_SY = 320, 240
WINDOW_X, WINDOW_Y = 100, 100

class GLAppBase(object):
    """This class represents skeleton of OpenGL programs."""

    def __init__(self, **kwargs):
        """Initialize an instance of class GLAppBase."""

        self.frame_count = 0
        self.context_version = kwargs.get(
            'context_version', CONTEXT_VERSION)
        self.window_title = kwargs.get(
            'window_title', WINDOW_TITLE)
        self.window_size = kwargs.get(
            'window_size', (WINDOW_SX, WINDOW_SY))
        self.window_position = kwargs.get(
            'window_position', (WINDOW_X, WINDOW_Y))

    def run(self, args):
        """Run a program."""

        self.init_glut(args)

        print("Vendor: {}\nRenderer: {}\nVersion: {}\nGLSL: {}".format(
            glGetString(GL_VENDOR).decode(),
            glGetString(GL_RENDERER).decode(),
            glGetString(GL_VERSION).decode(),
            glGetString(GL_SHADING_LANGUAGE_VERSION).decode()),
              file=sys.stderr, flush=True)

        self.init_program()
        self.init_gl()
        self.init_object()

        return glutMainLoop()

    def init_glut(self, args):
        """Initialize the GLUT state."""

        # Initialize GLUT.
        glutInit(args)

        glutInitContextVersion(
            self.context_version[0], self.context_version[1])
        glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
        glutInitContextProfile(GLUT_CORE_PROFILE)

        glutSetOption(
            GLUT_ACTION_ON_WINDOW_CLOSE,
            GLUT_ACTION_GLUTMAINLOOP_RETURNS)

        # Initialize and create the main window.
        glutInitDisplayMode(
            GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(
            self.window_size[0], self.window_size[1])
        glutInitWindowPosition(
            self.window_position[0], self.window_position[1])
        glutCreateWindow(self.window_title)

        glutDisplayFunc(self.render)
        glutIdleFunc(self.idle)
        glutReshapeFunc(self.resize)
        glutKeyboardFunc(self.keyboard)
        glutTimerFunc(0, self.timer, 0)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutCloseFunc(self.cleanup)

    def init_program(self):
        """Setup shaders."""
        pass

    def init_gl(self):
        """Initialize the OpenGL state."""

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def init_object(self):
        """Override this method."""
        pass

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        glViewport(0, 0, width, height)

    def render(self):
        """The display callback function."""

        self.frame_count += 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.do_render()
        glutSwapBuffers()

    def timer(self, value):
        """The timer callback function."""

        if value != 0:
            caption = '{}: {} frames per secound @ {} x {}'.format(
                self.window_title.decode(),
                self.frame_count * 4,
                glutGet(GLUT_WINDOW_WIDTH),
                glutGet(GLUT_WINDOW_HEIGHT))

            glutSetWindowTitle(caption)

        self.frame_count = 0
        glutTimerFunc(250, self.timer, 1) # a quarter of a second

    def idle(self):
        """The idle callback function."""
        glutPostRedisplay()

    def keyboard(self, key, x, y):
        """The new keyboard callback function."""

        if ord(key) == 0o33:
            print('Exit', file=sys.stderr, flush=True)
            sys.exit()

        glutPostRedisplay()

    def mouse(self, button, state, x, y):
        """The mouse callback function."""
        pass

    def motion(self, x, y):
        """The motion callback function."""
        pass

    def cleanup(self):
        """The clean up callback function."""
        pass

    def do_render(self):
        """Override this method."""
        pass

def main(args):
    """The main function."""
    app = GLAppBase()
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
