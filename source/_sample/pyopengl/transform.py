#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""transform.py: 

Reference:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
  * OpenGLBook.com
    <http://openglbook.com/chapter-4-entering-the-third-dimension.html>
  * Tutorials for modern OpenGL (3.3+)
    <http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/>
  * DGL WIKI
    <http://wiki.delphigl.com/index.php/gluPerspective>
    <http://wiki.delphigl.com/index.php/gluLookAt>
"""
import sys
import numpy as np
from numpy.linalg import norm

def scale(x, y, z):
    """Imitate glScale"""

    return np.diag([x, y, z, 1.])

def translate(x, y, z):
    """Imitate glTranslate"""

    mat = np.identity(4)
    mat[0, 3] = x
    mat[1, 3] = y
    mat[2, 3] = z
    mat[3, 3] = 1.

    return mat

def lookat(eye, center, up):
    """Imitate gluLookAt"""

    f = center - eye
    f /= norm(f)

    s = np.cross(f, up)
    s /= norm(s)

    u = np.cross(s, f)

    mat = np.identity(4)
    mat[0, :3] = s
    mat[1, :3] = u
    mat[2, :3] = -f

    mat[0, 3] = np.dot(-eye, s)
    mat[1, 3] = np.dot(-eye, u)
    mat[2, 3] = np.dot(-eye, -f)

    return mat

def perspective(fovy, aspect, znear, zfar):
    """Imitate gluPerspective"""

    f = 1.0 / np.tan(fovy * (np.pi / 360))
    delta = znear - zfar

    mat = np.identity(4)
    mat[0, 0] = f / aspect
    mat[1, 1] = f
    mat[2, 2] = (zfar + znear) / delta
    mat[2, 3] = (2 * zfar * znear) / delta
    mat[3, 2] = -1
    mat[3, 3] = 0

    return mat
