#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""appbase.py: Define class AppBase.

Reference:
  * rndblnch / opengl-programmable <bitbucket.org/rndblnch/opengl-programmable>
  * Simple Demo for GLSL <www.lighthouse3d.com>
  * OpenGLBook.com <openglbook.com>
"""

# pylint: disable=unused-argument,no-self-use
# pylint: disable=invalid-name
import sys
from abc import ABCMeta
from abc import abstractmethod
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
from Quaternion import Quat
from viewnavigation import ViewRotate
from viewnavigation import ViewZoom

CONTEXT_VERSION = (3, 1)
WINDOW_TITLE = b"PyOpenGL Demo"
WINDOW_SX, WINDOW_SY = (320, 240)
WINDOW_X, WINDOW_Y = (100, 100)
PERSPECTIVE_FOVY = 45.0
PERSPECTIVE_NEAR = 1.0
PERSPECTIVE_FAR = 100.0
CAMERA_EYE = (0., 10., 0.)
CAMERA_CENTER = (0., 0., 0.)
CAMERA_UP = (0., 1., 0.)

# pylint: disable=abstract-class-not-used
class AppBase(metaclass=ABCMeta):
    """This class represents skeleton of OpenGL programs."""

    def __init__(self, **kwargs):
        """Initialize an instance of class AppBase."""

        self.frame_count = 0

        # parameters for GLUT
        self.context_version = kwargs.get(
            'context_version', CONTEXT_VERSION)
        self.window_title = kwargs.get(
            'window_title', WINDOW_TITLE)
        self.window_size = kwargs.get(
            'window_size', (WINDOW_SX, WINDOW_SY))
        self.window_position = kwargs.get(
            'window_position', (WINDOW_X, WINDOW_Y))

        self.mouse_event_handlers = []

        # paramters for gluPerspective/perspective
        self.fovy = kwargs.get('perspective_fovy', PERSPECTIVE_FOVY)
        self.znear = kwargs.get('perspective_near', PERSPECTIVE_NEAR)
        self.zfar = kwargs.get('perspective_far', PERSPECTIVE_FAR)

        # parameters for gluLookAt/lookat
        self.camera_eye = kwargs.get('camera_eye', CAMERA_EYE)
        self.camera_center = kwargs.get('camera_center', CAMERA_CENTER)
        self.camera_up = kwargs.get('camera_up', CAMERA_UP)

        # parameters for glMultMatrix
        self.quat = Quat([0., 0., 0., 1.])

        self.program_manager = None

    def run(self, args):
        """Run a program."""

        self.init_glut(args)
        self.init_program()
        self.init_gl()
        self.init_mouse_event_handlers()
        self.init_texture()
        self.init_object()
        self.init_transform()

        return GLUT.glutMainLoop()

    def init_glut(self, args):
        """Initialize the GLUT state."""

        # Initialize GLUT.
        GLUT.glutInit(args)

        GLUT.glutInitContextVersion(
            self.context_version[0], self.context_version[1])
        GLUT.glutInitContextFlags(GLUT.GLUT_FORWARD_COMPATIBLE)
        GLUT.glutInitContextProfile(GLUT.GLUT_CORE_PROFILE)

        GLUT.glutSetOption(
            GLUT.GLUT_ACTION_ON_WINDOW_CLOSE,
            GLUT.GLUT_ACTION_GLUTMAINLOOP_RETURNS)

        # Initialize and create the main window.
        GLUT.glutInitDisplayMode(
            GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH)
        GLUT.glutInitWindowSize(
            self.window_size[0], self.window_size[1])
        GLUT.glutInitWindowPosition(
            self.window_position[0], self.window_position[1])
        GLUT.glutCreateWindow(self.window_title)

        GLUT.glutDisplayFunc(self.render)
        GLUT.glutIdleFunc(self.idle)
        GLUT.glutReshapeFunc(self.resize)
        GLUT.glutKeyboardFunc(self.keyboard)
        GLUT.glutTimerFunc(0, self.timer, 0)
        GLUT.glutMouseFunc(self.mouse)
        GLUT.glutMotionFunc(self.motion)
        GLUT.glutCloseFunc(self.cleanup)

        aspects = [('Vendor', GL.GL_VENDOR),
                   ('Renderer', GL.GL_RENDERER),
                   ('Version', GL.GL_VERSION),]
        if self.context_version[0] > 1:
            aspects.append(('GLSL', GL.GL_SHADING_LANGUAGE_VERSION))

        for i in aspects:
            print('{}: {}'.format(i[0],
                                  GL.glGetString(i[1]).decode()),
                  file=sys.stderr, flush=True)

    @abstractmethod
    def init_program(self):
        """Setup shaders."""
        pass

    @abstractmethod
    def get_shader_sources(self):
        """Return shader sources."""
        return None

    def init_mouse_event_handlers(self):
        """Initialize view nagivation"""

        self.mouse_event_handlers.append(
            ViewRotate(self, GLUT.GLUT_LEFT_BUTTON))
        self.mouse_event_handlers.append(
            ViewZoom(self, GLUT.GLUT_RIGHT_BUTTON))

    def init_gl(self):
        """Initialize the OpenGL state."""

        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)

    def init_object(self):
        """Override this method."""
        pass

    def init_texture(self):
        """Initialize textures."""
        pass

    def init_transform(self):
        """Initialize VM transforms."""
        pass

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        GL.glViewport(0, 0, width, height)
        self.update_projection(self.fovy, width, height)

    def update_projection(self, fovy, width, height):
        """Set the projection matrix."""
        pass

    def update_rotation(self, quat=None):
        """Update the model transform."""
        pass

    def render(self):
        """The display callback function."""

        self.frame_count += 1
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        self.do_render()
        GLUT.glutSwapBuffers()

    def timer(self, value):
        """The timer callback function."""

        if value != 0:
            caption = '{}: {} frames per secound @ {} x {}'.format(
                self.window_title.decode(),
                self.frame_count * 4,
                GLUT.glutGet(GLUT.GLUT_WINDOW_WIDTH),
                GLUT.glutGet(GLUT.GLUT_WINDOW_HEIGHT))

            GLUT.glutSetWindowTitle(caption)

        self.frame_count = 0
        GLUT.glutTimerFunc(250, self.timer, 1) # a quarter of a second

    def idle(self):
        """The idle callback function."""
        GLUT.glutPostRedisplay()

    def keyboard(self, key, x, y):
        """The new keyboard callback function."""

        if ord(key) == 0o33:
            print('Exit', file=sys.stderr, flush=True)
            sys.exit()

        GLUT.glutPostRedisplay()

    def mouse(self, button, state, x, y):
        """The mouse callback function."""

        for handler in self.mouse_event_handlers:
            handler.mouse(button, state, x, y)

    def motion(self, x, y):
        """The motion callback function."""

        for handler in self.mouse_event_handlers:
            handler.motion(x, y)

    def cleanup(self):
        """The clean up callback function."""
        pass

    def do_render(self):
        """Override this method."""
        pass

if __name__ == "__main__":
    pass
