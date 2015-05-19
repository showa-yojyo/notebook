#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
import sys
from os.path import dirname
from os.path import join
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = uic.loadUi(join(dirname(__file__), 'myform.ui'))

    window.show()
    sys.exit(app.exec_())
