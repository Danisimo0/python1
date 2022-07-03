import time
import sys
from threading import Thread
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QWidget, QLabel, QVBoxLayout, QDialogButtonBox, QDialog, QApplication)
from PySide6.examples.webenginewidgets.markdowneditor.ui_mainwindow import Ui_MainWindow
import os


def reset_timer(self):
    self.hours = 0
    self.minutes = 0
    self.seconds = 0
    self.lable_path_hours.setText(str(self.hours))
    self.lable_path_minutes.setText(str(self.minutes))
    self.lable_path_seconds.setText(str(self.seconds))


def stop_timer(self):
    self.pause = False


def start_timer(self):
    self.pause = True
    self.hours = self.hours
    self.minutes = self.minutes
    self.seconds = self.seconds

    while self.pause:
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0
            if self.minutes > 59:
                self.hours += 1
                self.minutes = 0
                if self.hours > 23:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0

        # self.pause = pause
        self.lable_path_hours.setText(str(self.hours))
        self.lable_path_minutes.setText(str(self.minutes))
        self.lable_path_seconds.setText(str(self.seconds))
        print(f"{self.hours}:{self.minutes}:{self.seconds}")


# main window**************************************************************************

class MainWindow(QWidget):
    def __init__(self, width, height, title):
        QWidget.__init__(self)
        self.start_new_thread = None
        self.setWindowTitle(title)
        self.resize(width, height)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        ##################################################################

        ##################################################################

        ##################################################################

        # ВНИМАНИЕ: ПОСМОТРИТЕ ПОЖАЛУЙСТА ПОЧЕМУ ТО У МЕНЯ ЗДЕСЬ ОШИБКА НЕ РАЗОБРАЛСЯ КУДА ВСТАВЛЯТЬ НУЖНО НАСТРОЙКИ ВИДЖЕТА
        # ***********************************************************************************************
        ##################################################################
        # может как то не правильно вставлял саму картинку ?
        # прошу если знаете ответ, написать в Телеграмме
        # width.setPixmap(QPixmap('C:\Project\projects\python1\temp\Новая папка'))
        # width.setScaledContents(True)

        ##################################################################
        ##################################################################
        # *******************************************
        self.pause = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        #################################
        self.lable_path_hours = QLabel("00")
        self.layout.addWidget(self.lable_path_hours, 0, 0)
        self.lable_path1 = QLabel(":")
        self.layout.addWidget(self.lable_path1, 0, 1)
        self.lable_path_minutes = QLabel("00")
        self.layout.addWidget(self.lable_path_minutes, 0, 2)
        self.lable_path2 = QLabel(":")
        self.layout.addWidget(self.lable_path2, 0, 3)
        self.lable_path_seconds = QLabel("00")
        self.layout.addWidget(self.lable_path_seconds, 0, 4)
        ####################################
        self.push_button_check = QPushButton('Start')
        self.push_button_check.clicked.connect(self.start_new_thread)
        self.layout.addWidget(self.push_button_check, 1, 1)
        self.push_button_check = QPushButton('Stop')
        self.push_button_check.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.push_button_check, 1, 2)
        self.push_button_check = QPushButton('Reset')
        self.push_button_check.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.push_button_check, 1, 3)
        #########################################
        self.show()

    def stop_timer(self):
        self.pause = False

    def reset_timer(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.lable_path_hours.setText(str(self.hours))
        self.lable_path_minutes.setText(str(self.minutes))
        self.lable_path_seconds.setText(str(self.seconds))

    def start_timer(self):
        self.pause = True
        self.hours = self.hours
        self.minutes = self.minutes
        self.seconds = self.seconds

        while self.pause:
            self.seconds += 1
            if self.seconds > 59:
                self.minutes += 1
                self.seconds = 0
                if self.minutes > 59:
                    self.hours += 1
                    self.minutes = 0
                    if self.hours > 23:
                        self.seconds = 0
                        self.minutes = 0
                        self.hours = 0

            time.sleep(0.01)
            # self.pause = pause
            self.lable_path_hours.setText(str(self.hours))
            self.lable_path_minutes.setText(str(self.minutes))
            self.lable_path_seconds.setText(str(self.seconds))
            print(f"{self.hours}:{self.minutes}:{self.seconds}")
            self.setCentralWidget(MainWindow)

    def start_new_thread(self):
        Thread(target=self.start_timer).start()

    def setCentralWidget(self, MainWindow):
        pass


app = QApplication(sys.argv)
Main_Window = MainWindow(640, 480, "Timer")
app.exec()

# пока разбирался с картинкой все упало, теперь вообще таймер не работает, ошибки не нашел
# игрался с виджитами
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         if not Form.objectName():
#             Form.setObjectName(u"Form")
#         Form.resize(417, 120)
#         self.gridLayout_2 = QGridLayout(Form)
#         self.gridLayout_2.setObjectName(u"gridLayout_2")
#         self.label = QLabel(Form)
#         self.label.setObjectName(u"label")
#         self.label.setMaximumSize(QSize(16777215, 50))
#         self.label.setAlignment(Qt.AlignCenter)
#         self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
#
#         self.pushButton = QPushButton(Form)
#         self.pushButton.setObjectName(u"pushButton")
#         self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
#
#         self.pushButton_2 = QPushButton(Form)
#         self.pushButton_2.setObjectName(u"pushButton_2")
#         self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
#
#         self.retranslateUi(Form)
#         QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#         self.label.setText(
#             QCoreApplication.translate("Form", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?", None))
#         self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u0430", None))
#         self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0442", None))
#
#
# class Widget(QWidget, Ui_Form):
#     def __init__(self):
#         super(Widget, self).__init__()
#         self.setupUi(self)
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(808, 510)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#
#         self.gridLayout = QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName(u"gridLayout")
#
#         self.frame = QFrame(self.centralwidget)
#         self.frame.setObjectName(u"frame")
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setFrameShadow(QFrame.Raised)
#
#         self.image_label = QLabel(alignment=Qt.AlignCenter)
#         self.image_label.setObjectName(u"image_label")
#         self.image_label.setPixmap(QPixmap("head3.png"))
#         lay = QVBoxLayout(self.frame)
#         lay.addWidget(self.image_label)
#
#         self.widget = QWidget(self.image_label)
#         self.widget.setObjectName(u"widget")
#
#         self.formLayout = QFormLayout(self.widget)  # - (self.frame)
#         self.formLayout.setObjectName(u"formLayout")
#
#         self.pushButton = QPushButton()  # - (self.frame)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setMinimumSize(QSize(50, 30))
#         self.pushButton.setMaximumSize(QSize(16777214, 16777215))
#         self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton)
#
#         self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Fixed)
#         self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer)
#         self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.retranslateUi(MainWindow)
#         QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Test", None))
#
#
# # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# class Dialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.parent = parent
#
#         lbl = QLabel("please click something ...")
#         buttonBox = QDialogButtonBox(
#             QDialogButtonBox.Cancel | QDialogButtonBox.Apply)
#
#         layout = QVBoxLayout(self)
#         layout.addWidget(lbl)
#         layout.addWidget(buttonBox)
#         self.resize(100, 50)
#
#         applyBtn = buttonBox.button(QDialogButtonBox.Apply)
#         applyBtn.clicked.connect(self.apply)
#         cancelBtn = buttonBox.button(QDialogButtonBox.Cancel)
#         cancelBtn.clicked.connect(self._reject)
#
#     def apply(self):
#         print("Dialog: in apply")
#
#     def _reject(self):
#         self.reject()
#         self.parent.close()
#
#     def closeEvent(self, event):
#         self.parent.close()
#
#
# class Window(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName(u"window")
#
#         self.dialog = Dialog(self)
#
#         gridLayout = QGridLayout(self)
#         gridLayout.addWidget(self.dialog, 1, 1, 1, 1)
#
#
# # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setMouseTracking(True)
#         self.setupUi(self)
#
#         # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#         self.pushButton.clicked.connect(self.create_dialog)
#
#     def create_dialog(self):
#         self.window = Window(self)
#         self.window.move(0, 0)
#         self.window.resize(self.size())
#         self.window.show()
#
#         self.window.dialog.show()
#
#
# # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
# Stylesheet = """
# #centralwidget {
#     background-color:  rgb(37, 237, 37);
# }
# #frame {
#     background-color:  rgb(37, 37, 237);
# }
#
# #pushButton {
#     background-color: rgba(233, 33, 33, 0.7);
#     color: #bfbfbf;
# }
# #image_label {
#     background-color:  rgb(137, 137, 237);
# }
# #window {
#     background-color: rgba(233, 33, 33, 0.5);
#     color: #bfbfbf;
# }
# """
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     app.setStyleSheet(Stylesheet)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
# def start_new_thread(self):
#     Thread(target=self.start_timer).start()
#
