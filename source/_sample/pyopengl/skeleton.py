#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A study program of OpenGL."""

# pylint: disable=unused-argument
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys

#import math
from argparse import ArgumentParser
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# NumPy
#from numpy import array

# Pillow
#from PIL import Image

# Here are constant variables.
window_title = b"OpenGL Study"
window_sx, window_sy = 320, 240
window_x, window_y = 100, 100

def init():
    """Initialize the OpenGL state."""

    glClearColor(0., 0., 0., 1.)
    glEnable(GL_DEPTH_TEST)

def display():
    """The display callback function.

    Returns:
      None
    """

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Render primitives.
    glPushAttrib(GL_CURRENT_BIT)

    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glEnd()

    glPopAttrib()
    glPopMatrix()

    # Swap rendering buffers to repaint the screen.
    glutSwapBuffers()

def reshape(width, height):
    """The reshape callback function.

    Args:
      width (int): the width of new window size in pixels.
      height (int): the width of new window size in pixels.

    Returns:
      None
    """
    if height == 0:
        return

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        # Portrait.
        aspect = height / width
        glOrtho(-2, 2, -2 * aspect, 2 * aspect, -5.0, 20.0)
    else:
        # Landscape.
        aspect = width / height
        glOrtho(-2 * aspect, 2 * aspect, -2, 2, -5.0, 20.0)

    # When you prefer perspective projection, use this:
    #gluPerspective(45.0, width / height, 1.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard(key, x, y):
    """The new keyboard callback function.

    Args:
      key (?): n The ASCII character that the user typed into the window.
      x (int): X coordinate of the mouse location in window relative
        coordinates when the key was pressed.
      y (int): Y coordinate of the mouse location in window relative
        coordinates when the key was pressed.

    Returns:
      None
    """

    if ord(key) == 0o33:
        # ESC
        print('ESC pressed', file=sys.stderr)
        sys.exit()

def mouse(button, state, x, y):
    """The mouse callback function.

    Args:
        button (int): One of GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON, or
          GLUT_RIGHT_BUTTON.
        state (int): either GLUT_UP or GLUT_DOWN.
        x (int): X of the window relative coordinates when the mouse button
          state changed.
        y (int): Y of the window relative coordinates when the mouse button
          state changed.

    Returns:
        None.
    """
    pass

def motion(x, y):
    """The motion callback function.

    Args:
        x (int): X of the mouse location in window relative coordinates.
        y (int): Y of the mouse location in window relative coordinates.

    Returns:
        None.
    """
    pass

def main(args):
    """The main function.

    Args:
        args: An instance which argparse.ArgumentParser.parse_args() returned.

    Returns:
        None.
    """

    # Initialize GLUT.
    glutInit(sys.argv)

    # Initialize and create the main window.
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_sx, window_sy)
    glutInitWindowPosition(window_x, window_y)
    glutCreateWindow(window_title)

    # Initialize the OpenGL state.
    init()

    # Register callback functions.
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    #glutMotionFunc(motion)

    glutMainLoop()

if __name__ == '__main__':
    parser = ArgumentParser(description='OpenGL Study')
    main(parser.parse_args())
