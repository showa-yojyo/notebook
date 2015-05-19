#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget

# pyuic5.bat myform.ui > ui_myform.py
from ui_myform import Ui_Form

class Form(QWidget, Ui_Form):
    """The third example shows the multiple inheritance approach."""

    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)

    def accept(self):
        QMessageBox.information(
            self,
            "Information",
            'checkState: %d\nselectedData: %s' % (
                self.checkBox.checkState(),
                self.calendarWidget.selectedDate().toString(
                    'yyyy/MM/dd (ddd)')),
            QMessageBox.Ok)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
