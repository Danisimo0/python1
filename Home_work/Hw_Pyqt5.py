# from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
#
# import sys
# import os
#
#
# class Window(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#
#         # setting title
#         self.setWindowTitle("Files ")
#         self.setGeometry(100, 100, 500, 400)
#         self.UiComponents()
#         self.initUI()
#         self.show()
#         self.btn.clicked.connect(self.on_click)
#
#     def clicked(self):
#         file = open("C:\Project\projects\python1\temp", "w")
#
#
#
#     def initUI(self):
#         qbtn = QPushButton('Button', self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(140, 120)
#
#         self.setGeometry(500, 200, 340, 300)
#         self.setWindowTitle('Quit button')
#         self.show()
#
#
#     def UiComponents(self):
#         # creating spin box
#         self.spin = QSpinBox(self)
#         self.spin.setGeometry(200, 70, 100, 30)
#         self.spin.setValue(0)
#
#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(App.exec())
#
my_file = open("file.txt", "w+")