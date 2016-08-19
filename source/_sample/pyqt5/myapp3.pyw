#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
"""myapp3.pyw: Use setupUI in a subclass of both QWidget and Ui_From.
"""
# pylint: disable=no-name-in-module
import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QWidget)

# pyuic5.bat myform.ui > ui_myform.py
from ui_myform import Ui_Form

class Form(QWidget, Ui_Form):
    """The third example shows the multiple inheritance approach."""

    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)

    def accept(self):
        """Event handler."""

        QMessageBox.information(
            self,
            'Information',
            'checkState: {}\nselectedData: {}'.format(
                self.checkBox.checkState(),
                self.calendarWidget.selectedDate().toString(
                    'yyyy/MM/dd (ddd)')),
            QMessageBox.Ok)
        self.close()

def main():
    """Main loop."""

    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
