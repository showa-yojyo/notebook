#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

# pyuic5.bat myform.ui > ui_myform.py
from ui_myform import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
