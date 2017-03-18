#!/usr/bin/env pythonw
"""myapp4.pyw: Directly load Widget from myform.ui.
"""
# pylint: disable=no-name-in-module
import sys
from os.path import (dirname, join)
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def main():
    """Directly load Widget from myform.ui."""

    app = QApplication(sys.argv)
    window = uic.loadUi(join(dirname(__file__), 'myform.ui'))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
