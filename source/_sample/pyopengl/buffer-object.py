#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""buffer-object.py: Demonstrate how to use buffer object APIs.

References:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
  * OpenGLBook.com
    <http://openglbook.com/chapter-3-index-buffer-objects-and-primitive-types.html>
"""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
import colorsys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import c_void_p
from glappbase import GLAppBase

class BufferObjectDemoApp(GLAppBase):
    """Demonstrate how to use buffer object APIs."""

    def __init__(self, **kwargs):
        """Initialize an instance of this class."""

        kwargs['context_version'] = (2, 1)
        super(BufferObjectDemoApp, self).__init__(**kwargs)
        self.buffer_id = 0
        self.index_buffer_id = None
        self.num_triangles = 24

    def init_object(self):
        """Initialize the object to be displayed."""

        num_triangles = self.num_triangles
        vertices = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        for i in range(num_triangles):
            theta = 2 * np.pi * i / num_triangles
            pos = np.array([np.cos(theta), np.sin(theta), 1.0, 1.0])
            color = colorsys.hsv_to_rgb(i / num_triangles, 1.0, 1.0)
            vertices = np.hstack((vertices, pos, color, [1.0]))

        vertices = vertices.astype(np.float32)
        indices = np.hstack((range(num_triangles + 1), 1)).astype(np.uint8)

        # Create buffer objects data.
        self.buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_id)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

        self.index_buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.index_buffer_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

        vertices_mem_size = np.nbytes[np.float32] * 4
        colors_mem_size = np.nbytes[np.float32] * 4
        unit_size = vertices_mem_size + colors_mem_size
        glVertexPointer(4, GL_FLOAT, unit_size, None)
        glColorPointer(4, GL_FLOAT, unit_size, c_void_p(vertices_mem_size))

    def do_render(self):
        """The display callback function."""

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glDrawElements(GL_TRIANGLE_FAN, self.num_triangles + 2, GL_UNSIGNED_BYTE, None)
        glPopClientAttrib()

    def cleanup(self):
        """The clean up callback function."""

        # Delete buffer objects.
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.buffer_id])

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.index_buffer_id])

def main(args):
    """The main function."""

    app = BufferObjectDemoApp(
        window_title=b"VBO",
        window_size=(300, 300))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
