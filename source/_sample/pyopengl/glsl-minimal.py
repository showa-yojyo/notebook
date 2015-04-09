#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""glsl-minimal.py: Demonstrate GLSL (with legacy API).

Reference:
  * rndblnch / opengl-programmable <bitbucket.org/rndblnch/opengl-programmable>
  * Simple Demo for GLSL <www.lighthouse3d.com>
"""
# pylint: disable=unused-argument
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from glappbase import GLAppBase

VERT_SHADER_SOURCE = """
void main()
{
    gl_Position = ftransform();
}
"""

FRAG_SHADER_SOURCE = """
void main()
{
     gl_FragColor = vec4(1., 0.07843137, 0.57647059, 1.);
}
"""

class GLSLMinimal(GLAppBase):
    """A minimal program which demonstrates GLSL."""

    def __init__(self, **kwargs):
        """Initialize an instance of class GLSLMinimal."""
        kwargs['context_version'] = (2, 1)
        super(GLSLMinimal, self).__init__(**kwargs)
        self.rotation = 0

    def init_program(self):
        """Setup shaders."""

        def create_shader(shader_type, source):
            """Compile a shader."""
            shader = glCreateShader(shader_type)
            glShaderSource(shader, source)
            glCompileShader(shader)
            if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
                raise RuntimeError(glGetShaderInfoLog(shader))
            return shader

        vert_shader = create_shader(GL_VERTEX_SHADER, VERT_SHADER_SOURCE)
        frag_shader = create_shader(GL_FRAGMENT_SHADER, FRAG_SHADER_SOURCE)

        program = glCreateProgram()
        glAttachShader(program, vert_shader)
        glAttachShader(program, frag_shader)

        glDeleteShader(vert_shader)
        glDeleteShader(frag_shader)

        glLinkProgram(program)
        if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(program))

        glUseProgram(program)

    def init_gl(self):
        """Initialize the OpenGL state."""

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def do_render(self):
        """Render the object."""

        glMatrixMode(GL_MODELVIEW)
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glPushMatrix()
        glLoadIdentity()
        gluLookAt(
            0.0, 0.0, 5.0,
            0.0, 0.0, -1.0,
            0.0, 1.0, 0.0)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, 0.5, 1, 0])
        glRotatef(self.rotation, 0, 1, 1)
        glutSolidTeapot(1)

        glPopAttrib()
        glPopMatrix()
        self.rotation += 0.1

    def resize(self, width, height):
        """The reshape callback function."""

        if height == 0:
            return

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glViewport(0, 0, width, height)

        gluPerspective(45, width / height, 1, 1000)

def main(args):
    """The main function."""

    app = GLSLMinimal(window_title=b"Simple Demo for GLSL")
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
