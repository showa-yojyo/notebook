#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from glappbase import GLAppBase

vertices = [[-1.0, -1.0,  1.0],
            [-1.0,  1.0,  1.0],
            [1.0,  1.0,  1.0],
            [1.0, -1.0,  1.0],
            [-1.0, -1.0, -1.0],
            [-1.0,  1.0,  -1.0],
            [1.0,  1.0,  -1.0],
            [1.0, -1.0,  -1.0]]

def drawtext(text, textwidth, textheight):

    img = Image.new('RGBA', (textwidth, textheight), 'white')
    dr = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('hgrme.ttc', 48, encoding='utf-8')

    width = 6
    height = 10
    for line in text.splitlines():
        ext = dr.textsize(line, fnt)
        dr.text((width, height), line, font=fnt, fill='black')
        width = max(ext[0], width)
        height += ext[1]

    return img

def polygon(a, b, c, d):
    glBegin(GL_POLYGON)

    glTexCoord2f(0.0, 0.0)
    glVertex3fv(vertices[a])

    glTexCoord2f(0.0, 1.0)
    glVertex3fv(vertices[b])

    glTexCoord2f(1.0, 1.0)
    glVertex3fv(vertices[c])

    glTexCoord2f(1.0, 0.0)
    glVertex3fv(vertices[d])
    glEnd()

class TextOnCubeDemo(GLAppBase):
    """Another demonstration of rendering text."""

    def __init__(self, **kwargs):
        """Initialize an instance of this class."""

        kwargs['context_version'] = (1, 5)
        super(TextOnCubeDemo, self).__init__(**kwargs)

    def init_gl(self):
        """Initialize the OpenGL state."""

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def init_object(self):
        """Initialize the object to be displayed."""

        textwidth, textheight = 64, 64
        img = drawtext('神', textwidth, textheight)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, textwidth, textheight, 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width / height, 1.0, 100.0)

    def do_render(self):
        """The display callback function."""

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        gluLookAt(4, 4, 3,
                  0, 0, 0,
                  0, 0, 1)

        glPushAttrib(GL_CURRENT_BIT)

        polygon(0, 3, 2, 1)
        polygon(2, 3, 7, 6)
        polygon(3, 0, 4, 7)
        polygon(1, 2, 6, 5)
        polygon(4, 5, 6, 7)
        polygon(5, 4, 0, 1)

        glPopAttrib()
        glPopMatrix()

def main(args):
    """The main function."""

    app = TextOnCubeDemo(window_title=b"God")
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
