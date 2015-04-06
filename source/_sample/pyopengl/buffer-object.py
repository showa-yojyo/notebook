#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""buffer-object.py: Demonstrate how to use buffer object APIs.

References:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
  * OpenGLBook.com
    <http://openglbook.com/chapter-3-index-buffer-objects-and-primitive-types.html>
"""
# pylint: disable=unused-argument
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
import colorsys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import c_void_p

WINDOW_TITLE = b"VBO"
WINDOW_SX, WINDOW_SY = 300, 300

class GLBufferObjectDemoApp(object):
    """Demonstrate how to use buffer object APIs."""

    def __init__(self):
        """Initialize an instance of this class."""

        self.buffer_id = 0
        self.index_buffer_id = None
        self.num_triangles = 24

    def run(self, args):
        """Run a program."""

        self.init_glut(args)
        self.init_gl()

        print("Vendor: {}\nRenderer: {}\nVersion: {}\nGLSL: {}".format(
            glGetString(GL_VENDOR).decode(),
            glGetString(GL_RENDERER).decode(),
            glGetString(GL_VERSION).decode(),
            glGetString(GL_SHADING_LANGUAGE_VERSION).decode()),
        file=sys.stderr, flush=True)

        return glutMainLoop()

    def init_glut(self, args):
        """Initialize the GLUT state."""

        glutInit(args)
        glutInitContextVersion(3, 1)
        glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
        glutInitContextProfile(GLUT_CORE_PROFILE)

        glutSetOption(
            GLUT_ACTION_ON_WINDOW_CLOSE,
            GLUT_ACTION_GLUTMAINLOOP_RETURNS)

        glutInitDisplayMode(
            GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_SX, WINDOW_SY)
        glutCreateWindow(WINDOW_TITLE)

        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        glutCloseFunc(self.cleanup)

    def init_gl(self):
        """Initialize the OpenGL state."""

        self.create_vbo()

        vertices_mem_size = np.nbytes[np.float32] * 4
        colors_mem_size = np.nbytes[np.float32] * 4
        unit_size = vertices_mem_size + colors_mem_size
        glVertexPointer(4, GL_FLOAT, unit_size, None)
        glColorPointer(4, GL_FLOAT, unit_size, c_void_p(vertices_mem_size))

        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        glViewport(0, 0, width, height)

    def render(self):
        """The display callback function."""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glDrawElements(GL_TRIANGLE_FAN, self.num_triangles + 2, GL_UNSIGNED_BYTE, None)
        glutSwapBuffers()

    def cleanup(self):
        """The clean up callback function."""

        self.destroy_vbo()

    def create_vbo(self):
        """Create buffer objects data."""

        num_triangles = self.num_triangles
        vertices = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        for i in range(num_triangles):
            theta = 2 * np.pi * i / num_triangles
            pos = np.array([np.cos(theta), np.sin(theta), 1.0, 1.0])
            color = colorsys.hsv_to_rgb(i / num_triangles, 1.0, 1.0)
            vertices = np.hstack((vertices, pos, color, [1.0]))

        vertices = vertices.astype(np.float32)
        indices = np.hstack((range(num_triangles + 1), 1)).astype(np.uint8)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        self.buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_id)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

        self.index_buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.index_buffer_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    def destroy_vbo(self):
        """Delete buffer objects."""

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.buffer_id])

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.index_buffer_id])

def main(args):
    """The main function."""
    app = GLBufferObjectDemoApp()
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
