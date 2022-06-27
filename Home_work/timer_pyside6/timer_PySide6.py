import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.timer = QTimer(self) #self
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count = 0

    def update(self):
        self.count += 1
        print ("update ",self.count)
        if self.count >5:
            self.timer.stop()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mymain = MainWidget()
    mymain.show()


hours = 0
minutes = 0
seconds = 0
pause = True


def stop_timer():
    global pause

    pause = False

def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours.config(text=f"{hours}")
    minuts.config(text=f"{minutes}")
    seconds.config(text=f"{seconds}")


def start_timer():
    global pause

    pause = True

    global hours
    # hours = 0
    global minutes
    # minutes = 0
    global seconds
    # seconds = 0

# код до цикла
    while pause:
# seconds = seconds + 1
     seconds += 1

    if seconds > 59:
     minutes += 1
     seconds = 0

    if minutes > 59:
      hours += 1
      minutes = 0

    if hours > 23:
      seconds = 0
      minutes = 0
      hours = 0

    time.sleep(0.00001)

    hours.config(text=f"{hours}")
    minuts.config(text=f"{minutes}")
    seconds.config(text=f"{seconds}")
    print(f"{hours}:{minutes}" + ":" + str(seconds))


    # определение(создание) функции
def start_new_thread():
    Thread(
        target=start_timer
    ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
        # будет виснуть


sys.exit(app.exec())