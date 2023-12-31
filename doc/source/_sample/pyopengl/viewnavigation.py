#!/usr/bin/env python
"""viewnavigation.py: Implement zooming and rotation.
"""
# pylint: disable=unused-argument, no-self-use, invalid-name, no-member
from abc import (ABCMeta, abstractmethod)
import numpy as np
from numpy.linalg import norm
import OpenGL.GLUT as GLUT
from Quaternion import Quat

# pylint: disable=too-few-public-methods
class AbstractViewNavigation(metaclass=ABCMeta):
    """The abstract base class of for classes that control view navigation."""

    def __init__(self, app, button):
        """Initialize an instance of class AbstractViewNavigation."""

        self.app = app
        self.button = button
        self.width = 0
        self.height = 0
        self.first_mouse_position = None

    def mouse(self, button, state, x, y):
        """The mouse callback function."""

        if button == self.button:
            if state == GLUT.GLUT_DOWN:
                self.capture_mouse(x, y)
            else:
                self.release_mouse()

    def motion(self, x, y):
        """The motion callback function."""

        if self.first_mouse_position:
            self.update_mouse_position(x, y)

    def capture_mouse(self, x, y):
        """Capture mouse drag event."""

        self.width = GLUT.glutGet(GLUT.GLUT_WINDOW_WIDTH)
        self.height = GLUT.glutGet(GLUT.GLUT_WINDOW_HEIGHT)
        self.first_mouse_position = nds_coord(x, y, self.width, self.height)

    def release_mouse(self):
        """Release mouse drag event."""
        self.first_mouse_position = None

    @abstractmethod
    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""
        pass

class ViewRotate(AbstractViewNavigation):
    """Implement trackball-like rotation."""

    def __init__(self, app, button):
        """Initialize an instance of class ViewRotate."""

        super(ViewRotate, self).__init__(app, button)
        self.quat = Quat(app.quat)
        self.last_quat_arg = None

    def capture_mouse(self, x, y):
        """Capture mouse."""

        super(ViewRotate, self).capture_mouse(x, y)
        self.last_quat_arg = trackball_space(x, y, self.width, self.height)

    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""

        # Compute position on hemisphere.
        cur_quat_arg = trackball_space(x, y, self.width, self.height)

        # Compute the change in position the hemisphere.
        diff = cur_quat_arg - self.last_quat_arg
        if (abs(diff) < 1e-2).all():
            return

        last_quat = Quat(np.resize(self.last_quat_arg, 4))
        cur_quat = Quat(np.resize(cur_quat_arg, 4))

        self.last_quat_arg = cur_quat_arg
        self.quat = self.quat * last_quat * cur_quat
        self.app.update_rotation(self.quat)

        GLUT.glutPostRedisplay()

class ViewZoom(AbstractViewNavigation):
    """Implement zooming."""

    def __init__(self, app, button):
        """Initialize an instance of class ViewZoom."""

        super(ViewZoom, self).__init__(app, button)

    def update_mouse_position(self, x, y):
        """Handle mouse motion event."""

        cur_pos = nds_coord(x, y, self.width, self.height)
        factor = np.exp((cur_pos[1] - self.first_mouse_position[1]) * -0.25)
        fovy = max(min(self.app.fovy * factor, 125), 25)
        self.app.update_projection(fovy, self.width, self.height)
        GLUT.glutPostRedisplay()

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
