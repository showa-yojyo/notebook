#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""program_manager.py: Define class ProgramManager.
"""
import OpenGL.GL as GL

class ProgramManager(object):
    """OpenGL shader program manager.

    This class managers a program object and its shader objects.
    """

    def __init__(self):
        """Initialize an instance of class ProgramManager."""

        self.program_id = 0
        self.shader_sources = None
        self.shader_ids = {}

    def setup(self, shader_sources):
        """Setup shaders."""

        if not shader_sources:
            return

        shader_ids = {}
        for shader_type, source in shader_sources.items():
            shader = GL.glCreateShader(shader_type)
            GL.glShaderSource(shader, source)
            GL.glCompileShader(shader)
            if GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS) != GL.GL_TRUE:
                raise RuntimeError(GL.glGetShaderInfoLog(shader).decode())
            shader_ids[shader_type] = shader

        self.shader_sources = shader_sources
        self.shader_ids = shader_ids

        self.program_id = GL.glCreateProgram()
        for shader in shader_ids.values():
            GL.glAttachShader(self.program_id, shader)

        GL.glLinkProgram(self.program_id)
        if GL.glGetProgramiv(self.program_id, GL.GL_LINK_STATUS) != GL.GL_TRUE:
            raise RuntimeError(GL.glGetProgramInfoLog(self.program_id).decode())

        GL.glUseProgram(self.program_id)

    def cleanup(self):
        """Clean up shaders and program."""

        if not self.shader_sources:
            return

        GL.glUseProgram(0)
        for shader in self.shader_ids.values():
            GL.glDetachShader(self.program_id, shader)
            GL.glDeleteShader(shader)
        GL.glDeleteProgram(self.program_id)
