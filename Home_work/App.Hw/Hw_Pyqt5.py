from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import os

from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.initUI()
        self.UiComponents()
        self.setGeometry(100, 100, 600, 400)
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)

        button = QPushButton('PyQt5 button', self)

        button.setGeometry(230, 80, 100, 40)


    def UiComponents(self):
        self.spin = QSpinBox(self)
        self.spin.setGeometry(340, 80, 100, 40)
        self.spin.valueChanged.connect(self.show_result)

        self.label = QLabel(self)
        self.label.setGeometry(100, 200, 200, 40)

    def show_result(self):
        value = self.spin.value()
        self.label.setText("Files : " + str(value))
        file_save()

    def file_save(self):
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text2save = str(text.get(1.0, END))
        f.write(text2save)
        f.close()
# немного не доделал
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
