#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
"""myapp2.pyw: Use setupUI in a subclass of QWidget.
"""
# pylint: disable=no-name-in-module
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)

# pyuic5.bat myform.ui > ui_myform.py
from ui_myform import Ui_Form

class Form(QWidget):
    """The second example shows the single inheritance approach where we
    sub-class QWidget and set up the user interface in the __init__() method.
    """

    def __init__(self):
        super(Form, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect up the buttons.
        self.ui.pushButton.clicked.connect(self.accept)

    def accept(self):
        """NOP"""
        pass

def main():
    """Main loop."""

    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
