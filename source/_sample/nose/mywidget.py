#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mywidget.py: Define class Widget for demonstration of Nose.
"""

class Widget(object):
    """A class."""

    def __init__(self, title):
        self._title = title
        self._size = (50, 50)

    def dispose(self):
        """A method."""
        pass

    def size(self):
        """A method."""
        return self._size

    def resize(self, size_x, size_y):
        """A method."""
        self._size = (size_x, size_y)
