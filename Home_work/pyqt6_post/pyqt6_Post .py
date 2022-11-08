import sys

import psycopg2 as psycopg2
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit

connect = "dbname='postgres' user='postgres' host='localhost' password='Gosamu11'"
connection = psycopg2.connect(connect)
cursor = connection.cursor()


def connect_def(connect):
    global connection
    global cursor
    connection = psycopg2.connect(connect)
    cursor = connection.cursor()


connect_def(connect)


# connect_def(connect)
# cursor.execute(f"""
#             INSERT INTO public."user"(
#             login, password)
#             VALUES ('123', '123');""")
# cursor.close()
#
# connection.commit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()
        self.setWindowTitle("Adding and returning from the database")

        layout = QVBoxLayout()

        button1 = QPushButton("Return all value in table todo_list_user database todo_list_database")
        button1.clicked.connect(self.select_all)
        button2 = QPushButton("Add data to database")
        button2.clicked.connect(self.insert_data)


        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Input new name")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Input new password")

        self.input_id = QLineEdit()
        self.input_id.setPlaceholderText("Input id")
        self.input_new_name = QLineEdit()
        self.input_new_name.setPlaceholderText("Input new name")
        self.input_new_password = QLineEdit()
        self.input_new_password.setPlaceholderText("Input new password")

        button3 = QPushButton("Change")
        button3.clicked.connect(self.update_data)

        button1.setStyleSheet(
            "QPushButton { padding: 5px 7px; text-align: center; }"
        )

        layout.addWidget(button1)
        layout.addWidget(self.input_name)
        layout.addWidget(self.input_password)
        layout.addWidget(button2)

        layout.addWidget(self.input_id)
        layout.addWidget(self.input_new_name)
        layout.addWidget(self.input_new_password)
        layout.addWidget(button3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update_data(self):
        if self.input_id.text() == "":
            print("Input id")
        else:
            connect_def(connect)
            cursor.execute(f"""
                    UPDATE public."user"
                    SET login='{self.input_new_name.text()}', password='{self.input_new_password.text()}'
                    WHERE  id={self.input_id.text()};
                    """)
            # print(f'{self.input_name.text()}', f'{self.input_password.text()}')
            cursor.close()
            connection.commit()
            self.input_new_name.setText("")
            self.input_new_password.setText("")
            self.input_id.setText("")
            print("Update")

    def select_all(self):
        connect_def(connect)
        cursor.execute(f"""
                                SELECT * FROM public."user"
                                """)
        data_tasks = cursor.fetchall()
        cursor.close()

        print(data_tasks)
        # print(self.input_text.text())

    def insert_data(self):
        connect_def(connect)
        cursor.execute(f"""
        INSERT INTO public."user"(
        login, password)
        VALUES ('{self.input_name.text()}', '{self.input_password.text()}');
        """)
        # print(f'{self.input_name.text()}', f'{self.input_password.text()}')
        cursor.close()
        connection.commit()

        self.input_name.setText("")
        self.input_password.setText("")
        print("Successfully added")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.setFixedSize(600, 500)
app.exec()