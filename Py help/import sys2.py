import sys
import time
import ftplib
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread, Signal, QTimer

class FTPThread(QThread):
    status_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.ftp = ftplib.FTP()
        self.running = True

    def run(self):
        while self.running:
            try:
                self.ftp.connect('127.0.0.1', 21)  # Укажите адрес вашего FTP сервера
                self.ftp.login('Admin', 'Amaralle35')  # Укажите ваши логин и пароль
                self.status_signal.emit(True)
                self.ftp.quit()
            except ftplib.all_errors as e:
                print(f"FTP Error: {e}")
                self.status_signal.emit(False)
            
            time.sleep(10)  # Ожидание 15 минут перед следующей попыткой подключения

    def stop(self):
        self.running = False
        self.wait()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FTP Connection Status")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.status_label = QLabel("Status: Not Connected")
        self.layout.addWidget(self.status_label)

        self.status_icon = QLabel()
        self.layout.addWidget(self.status_icon)

        self.ftp_thread = FTPThread()
        self.ftp_thread.status_signal.connect(self.update_status)
        self.ftp_thread.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_connection)
        self.timer.start(60000)  # Обновление статуса каждую минуту

        self.connection_attempts = 0

    def update_status(self, connected):
        if connected:
            self.status_label.setText("Status: Connected")
            self.status_icon.setPixmap(QPixmap("green.png"))  # Укажите путь к зеленой картинке
            self.connection_attempts = 0
        else:
            self.status_label.setText("Status: Not Connected")
            self.status_icon.setPixmap(QPixmap("red.png"))  # Укажите путь к красной картинке
            self.connection_attempts += 1
            if self.connection_attempts >= 3:
                self.ftp_thread.stop()
                self.timer.stop()

    def check_connection(self):
        if not self.ftp_thread.isRunning():
            self.ftp_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())