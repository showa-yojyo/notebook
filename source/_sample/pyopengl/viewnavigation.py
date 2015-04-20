#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""viewnavigation.py: Implement zooming and rotation.
"""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
from abc import ABCMeta
from abc import abstractmethod
import numpy as np
from numpy.linalg import norm
from OpenGL.GLUT import *
from Quaternion import Quat

# pylint: disable=too-few-public-methods
class AbstractViewNavigation(metaclass=ABCMeta):
    """The abstract base class of for classes that control view navigation."""

    def __init__(self, app, x, y):
        """Initialize an instance of class AbstractViewNavigation."""

        self.app = app
        self.width = glutGet(GLUT_WINDOW_WIDTH)
        self.height = glutGet(GLUT_WINDOW_HEIGHT)
        self.first_mouse_position = nds_coord(x, y, self.width, self.height)

    @abstractmethod
    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""
        return False

class ViewRotate(AbstractViewNavigation):
    """Implement trackball-like rotation."""

    def __init__(self, app, x, y):
        """Initialize an instance of class ViewRotate."""

        super(ViewRotate, self).__init__(app, x, y)
        self.last_quat_arg = trackball_space(x, y, self.width, self.height)

    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""

        # Compute position on hemisphere.
        cur_quat_arg = trackball_space(x, y, self.width, self.height)

        # Compute the change in position the hemisphere.
        diff = cur_quat_arg - self.last_quat_arg
        if (abs(diff) < 1e-2).all():
            return False

        last_quat = Quat(np.resize(self.last_quat_arg, 4))
        cur_quat = Quat(np.resize(cur_quat_arg, 4))

        self.last_quat_arg = cur_quat_arg
        self.app.quat = self.app.quat * last_quat * cur_quat
        self.app.update_model_transform()

        return True

class ViewZoom(AbstractViewNavigation):
    """Implement zooming."""

    def __init__(self, app, x, y):
        """Initialize an instance of class ViewZoom."""
        super(ViewZoom, self).__init__(app, x, y)

    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""

        cur_mouse_position = nds_coord(x, y, self.width, self.height)
        factor = np.exp(cur_mouse_position[1] - self.first_mouse_position[1])
        factor *= -0.25
        fovy = max(min(self.app.fovy * factor, 125), 25)
        self.app.fovy = fovy
        self.app.update_perspective(self.width, self.height)

        return True

def nds_coord(x, y, width, height):
    """Convert SCS to NDS."""
    return (2 * x - width) / width, (height - 2 * y) / height

def trackball_space(x, y, width, height):
    """Project orthographically the mouse cursor to a hemisphere."""

    v = np.zeros(4)
    v[0], v[1] = nds_coord(x, y, width, height)
    d = np.dot(v, v) # length-squared

    if d < 1:
        v[2] = np.cos(d * np.pi / 2)
    else:
        v[2] = 0

    return v / norm(v)
