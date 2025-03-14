import sys
import time
import threading
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QProgressBar, QPushButton
from PySide2.QtCore import QTimer, Qt
from PySide2.QtGui import QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ftplib import FTP

class FTPClientApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FTP Client")
        self.setGeometry(100, 100, 800, 600)

        self.ftp = None
        self.connected = False
        self.downloading = False
        self.download_progress = 0

        self.init_ui()

        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(60000)  # Обновление статуса каждую минуту

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.status_label = QLabel("Статус подключения: Не подключено")
        self.status_label.setStyleSheet("color: red")
        layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.download_button = QPushButton("Скачать файл")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Скорость загрузки")
        self.ax.set_xlabel("Время")
        self.ax.set_ylabel("Скорость (KB/s)")
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-')

    def update_status(self):
        if self.connected:
            self.status_label.setText("Статус подключения: Подключено")
            self.status_label.setStyleSheet("color: green")
        else:
            self.status_label.setText("Статус подключения: Не подключено")
            self.status_label.setStyleSheet("color: red")

    def connect_to_ftp(self):
        try:
            self.ftp = FTP('127.0.0.1')
            self.ftp.login(user='Admin', passwd='Amaralle35')
            self.connected = True
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            self.connected = False

    def start_download(self):
        if not self.connected:
            print("Не подключено к FTP-серверу")
            return

        self.downloading = True
        self.download_progress = 0
        self.progress_bar.setValue(0)

        threading.Thread(target=self.download_file, daemon=True).start()

    def download_file(self):
        filename = 'your_file_to_download.txt'
        total_size = self.ftp.size(filename)
        downloaded_size = 0

        with open(filename, 'wb') as local_file:
            def callback(data):
                nonlocal downloaded_size
                local_file.write(data)
                downloaded_size += len(data)
                self.download_progress = int((downloaded_size / total_size) * 100)
                self.progress_bar.setValue(self.download_progress)

                speed = len(data) / 1024  # Скорость в KB/s
                self.update_speed_graph(speed)

            self.ftp.retrbinary(f'RETR {filename}', callback)

        self.downloading = False

    def update_speed_graph(self, speed):
        self.x_data.append(time.time())
        self.y_data.append(speed)

        if len(self.x_data) > 60:  # Ограничиваем график последними 60 точками
            self.x_data.pop(0)
            self.y_data.pop(0)

        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FTPClientApp()
    window.show()
    sys.exit(app.exec_())