
import os
import sys
import time

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QSpinBox


class MainWindow(QWidget):
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.label_check = QLabel('Enter files: ( .xlsx, ) ; ( .pptx, ) ; ( .docx ) ) ')
        self.layout.addWidget(self.label_check, 10, 0)

        self.line_edit_path = QLineEdit('.docx')
        self.layout.addWidget(self.line_edit_path, 1, 0)

        self.widget = QSpinBox()
        self.widget.setRange(1, 11111)
        self.widget.setSingleStep(1)
        self.layout.addWidget(self.widget, 0, 0)

        self.push_button_create = QPushButton('Create')
        self.layout.addWidget(self.push_button_create, 3, 0)
        self.push_button_create.clicked.connect(self.create)

        self.show()

    def create(self):
        spin_box_item = self.widget.value()
        input_get_expansion_item = self.line_edit_path.text()
        expansion = [".xlsx", ".pptx", ".docx"]

        def create_files():
            if input_get_expansion_item in expansion:
                for i in range(1, int(spin_box_item) + 1):
                    new_file = open(f"temp/file{i}{input_get_expansion_item}", "w+")
                    new_file.write("Write to me")
                    new_file.close()
                    self.label_check.setText("Files created")
                    time.sleep(1)
            else:
                self.label_check.setText("Files incorrectly")

        if os.path.isdir('temp'):
            create_files()
        else:
            os.mkdir("temp")
            create_files()


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'My App')
app.exec()



    #                                              My attempts





# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
# import sys
# import PySide6.QtWidgets as QtWidgets
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
#

#
# class MainWindow(QWidget):
#     def __init__(self, window_name: str):
#         super().__init__()
#
#         self.window_name = window_name
#         self.setGeometry(640, 480, 640, 480)
#         self.setWindowTitle(self.window_name)
#         self.layout = QtWidgets.QGridLayout()
#
#         self.button = QPushButton("button")
#         self.button.clicked.connect(self.create_files)
#         self.setCentralWidget(self.button)
#
#     # def create_files(self, amount=10):
#     #     for num in range(1, amount + 1):
#     #         with open(f'temp\new_file{num}.txt', 'w') as file:
#     #             file.write('.txt')
#
#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     main = MainWindow()
#     sys.exit(App.exec_())


# class ExampleWindow(QMainWindow):
#     def __init__(self, window_name: str):
#         super().__init__()
#
#         self.window_name = window_name
#         self.setGeometry(640, 480, 640, 480)
#         self.setWindowTitle(self.window_name)
#         self.layout = QtWidgets.QGridLayout()
#
#         self.button = QPushButton("Press Me!")
#         self.button.setGeometry(230, 80, 100, 40)
#
#         self.button.clicked.connect(self.create_files)
#         self.setCentralWidget(self.button)
#
#     def create_files(self, amount=10):
#         for num in range(1, amount + 1):
#             with open(f'Temp_hw/new_file{num}.txt', 'w') as file:
#                 file.write('')
#         print('done')
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = ExampleWindow('Наше приложение на PySide6')
#     ex.show()
#     sys.exit(app.exec())
