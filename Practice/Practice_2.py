# Есть файл (ШАБЛОН), Excel,в который нужно заполнить данные, сохраняя дизайн из шаблона, сами данные нужно сгенирировать range 5-5
# в центр, при измене шаблона, код должен не падать,

import openpyexcel

workbook = openpyexcel.load_workbook("dist/file_.xlsx")
worksheet = workbook.active

# print(worksheet.cell(1, 1).value)

max_row = worksheet.max_row
max_column = worksheet.max_column

for row in range(1, max_row + 1):
    for column in range(1, max_column + 1):
        match str(worksheet.cell(row, column).value):
            case "Js":
                worksheet.cell(row=row, column=column)
            case "Java":
                worksheet.cell(row=row, column=column)
            case "Python":
                worksheet.cell(row=row, column=column)
        print(f"{row} {column} {worksheet.cell(row, column).value}")
workbook.save("dist/file_.xlsx")
workbook.close()




















# Получить данные jsonplaceholder posts, записать в 1 https://jsonplaceholder.typicode.com/todos/1
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())
# with open("new.json", "w") as json_1:
#     json.dump(response.json(), json_1)


#     json_1.write(response.json())

#
# from PyQt6.QtCore import QSize
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout
# import sys
# import time
#
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.timer)
#         layout = QGridLayout()
#         layout.addWidget(self.button, 2, 0, 1, 1)
#         self.setFixedSize(QSize(480, 300))
#
#         # Устанавливаем центральный виджет Window.
#         self.setCentralWidget(self.button)
#
#     def timer(self):
#         index = 1
#         while True:
#             index += 1
#             time.sleep(0.5)
#             print(index)
#
#
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# app.exec()
#
# import sys

# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget,
# )

#
# # Подкласс QMainWindow для настройки основного окна приложения
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Widgets App")
#
#         layout = QVBoxLayout()
#         widgets = [
#
#
#
#
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLCDNumber,
#             QLabel,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit,
#         ]
#
#         for w in widgets:
#             layout.addWidget(w())
#
#         widget = QWidget()
#         widget.setLayout(layout)
#
#         # Устанавливаем центральный виджет окна. Виджет будет расширяться по умолчанию,
#         # заполняя всё пространство окна.
#         self.setCentralWidget(widget)
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
#
# app.exec()
#
#
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout
# import sys
# import time
#
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         self.button1 = QPushButton('Start')
#         self.button2 = QPushButton('Stop')
#         layout = QGridLayout()
#         layout.addWidget(self.button1, 2, 0, 1, 1)
#         layout.addWidget(self.button2, 2, 1, 1, 1)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
#
# class Calk:
#     def __init__(self, view):
#         self.view = view
#         self.duration = 5
#         self.view.button1.button2.connect(self.show)
#
#     def show(self):
#         self.view.show()
#         self.timer =
# if __name__ == "main":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())


# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow, self).__init__()
#
#         self.setWindowTitle("My App")
#
#         widget = QCheckBox()
#         widget.setCheckState(Qt.CheckState.Checked)
#
#         # Включение трёх состояний: widget.setCheckState(Qt.PartiallyChecked)
#         # Или: widget.setTriState(True)
#         widget.stateChanged.connect(self.show_state)
#
#         self.setCentralWidget(widget)
#
#
#     def show_state(self, s):
#         print(s == Qt.CheckState.Checked)
#         print(s)
#



