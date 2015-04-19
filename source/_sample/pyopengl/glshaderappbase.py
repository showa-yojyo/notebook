#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""glshaderappbase.py: Demonstrate GLSL (with legacy API).

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

class GLShaderAppBase(GLAppBase):
    """A minimal program which demonstrates GLSL."""

    def __init__(self, **kwargs):
        """Initialize an instance of class GLShaderAppBase."""

        kwargs.setdefault('context_version', (2, 1))
        super(GLShaderAppBase, self).__init__(**kwargs)

        self.shader_sources = {}
        self.shader_ids = {}
        self.program_id = 0

        self.rotation = 0

    def init_program(self):
        """Setup shaders."""

        self.init_shader_source()
        if not self.shader_sources:
            return

        shader_ids = {}
        for type, source in self.shader_sources.items():
            shader = glCreateShader(type)
            glShaderSource(shader, source)
            glCompileShader(shader)
            if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
                raise RuntimeError(glGetShaderInfoLog(shader).decode())
            shader_ids[type] = shader
        self.shader_ids = shader_ids

        self.program_id = glCreateProgram()
        for shader in shader_ids.values():
            glAttachShader(self.program_id, shader)

        glLinkProgram(self.program_id)
        if glGetProgramiv(self.program_id, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(self.program_id).decode())

        glUseProgram(self.program_id)

    def init_shader_source(self):
        """Initialize shader source."""

        self.shader_sources = {
            GL_VERTEX_SHADER: VERT_SHADER_SOURCE,
            GL_FRAGMENT_SHADER: FRAG_SHADER_SOURCE,}
        self.shader_ids = {}

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

    def cleanup(self):
        """The clean up callback function."""

        self.destroy_shaders()

    def destroy_shaders(self):
        """Clean up shaders."""

        if not self.shader_sources:
            return

        glUseProgram(0)
        for shader in self.shader_ids.values():
            glDetachShader(self.program_id, shader)
            glDeleteShader(shader)
        glDeleteProgram(self.program_id)

def main(args):
    """The main function."""

    app = GLShaderAppBase(
        context_version=(2, 1),
        window_title=b"Simple Demo for GLSL",)
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
