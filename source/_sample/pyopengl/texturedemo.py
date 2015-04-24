#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""texturedemo.py: Demonstrate how to use OpenGL texture (bitmap)."""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
import os
from glappbase import GLAppBase
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

class TextureDemoApp(GLAppBase):
    """Demonstrate how to use OpenGL texture (bitmap)."""

    def __init__(self, **kwargs):
        """Initialize an instance of class TextureDemoApp."""

        kwargs['context_version'] = (1, 5)
        super(TextureDemoApp, self).__init__(**kwargs)

    def init_gl(self):
        """Initialize the OpenGL state."""

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def init_object(self):
        """Initialize the object to be displayed."""

        source_path = os.path.join(
            os.path.dirname(__file__), '../pillow/illvelo.png')
        img = Image.open(source_path).resize((256, 256))
        assert img.mode == 'RGBA'

        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1],
            0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        vx, vy = 40.0, 40.0
        tx, ty = 6.0, 6.0

        vertices = (
            -vx, -vy, 0.0,
            vx, -vy, 0.0,
            vx, vy, 0.0,
            -vx, vy, 0.0,)

        texcoords = (
            -tx, -ty,
            tx, -ty,
            tx, ty,
            -tx, ty,)

        colors = (
            0, 0, 0, 0.75,
            0, 0, 0, 0.75,
            1, 1, 1, 0.75,
            0, 0, 0, 0.75,)

        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glTexCoordPointer(2, GL_FLOAT, 0, texcoords)
        glColorPointer(4, GL_FLOAT, 0, colors)

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width / height, 1.0, 100.0)

    def do_render(self):
        """Render the object."""

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        gluLookAt(14, 14, 1.58,
                  0, 0, 0,
                  0, 0, 1)

        glPushAttrib(GL_CURRENT_BIT)
        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glDrawArrays(GL_POLYGON, 0, 4)

        glPopClientAttrib()
        glPopAttrib()
        glPopMatrix()

def main(args):
    """The main function."""

    app = TextureDemoApp(
        window_title=b"Build texture from a PNG file",
        window_size=(320, 240))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
