#!/usr/bin/env pythonw
"""myapp1.pyw: Create an instance of Ui_Form.
"""
# pylint: disable=no-name-in-module
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)

# pyuic5.bat myform.ui > ui_myform.py
from ui_myform import Ui_Form

def main():
    """Main loop."""

    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
