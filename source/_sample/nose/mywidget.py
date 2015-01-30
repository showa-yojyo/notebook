# -*- coding: utf-8 -*-

class Widget(object):
    def __init__(self, title):
        self.title = title
        self.sz = (50, 50)

    def dispose(self):
        pass

    def size(self):
        return self.sz

    def resize(self, sx, sy):
        self.sz = (sx, sy)
