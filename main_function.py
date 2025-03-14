##############################################################################
####Imports lib###
from PySide2 import QtCore, QtWidgets, QtGui
import sys,os,time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import ftplib

##############################################################################
###Import interface file###
from interface_ui import *
from Custom_Widgets import *
#FLOWs
class FTPThread(QThread):
    status_signal = Signal(bool)
    def __init__(self):
        super().__init__()
        self.ftp = ftplib.FTP()
        self.running = True
    #Connect FTP Server
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
    #Reconect FTP Server STOP
    def stop(self):
        self.running = False
        self.wait()
#MAIN init  
class Main_Functions(QMainWindow):
    def __init__(self, object2):
        QMainWindow.__init__(self)
        self.main_func = object2
        #Запуск потока подключения к FTP
        self.ftp_thread = FTPThread()
        self.ftp_thread.status_signal.connect(self.update_status)
        self.ftp_thread.start()
        #timer Status connect FTP server
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_connection)
        self.timer.start(60000)  # Обновление статуса каждую минуту
        ###Clock timers
        self.clock_updater = QTimer(self)
        self.clock_updater.timeout.connect(self.update_clock)
        self.clock_updater.start(100)  # Обновление каждую секунду
        #ftp conection value parametrs
        self.connection_attempts = 0
    ###Clock function
    def update_clock(self):
        self.time = QTime.currentTime()
        self.txt_clock = self.time.toString('hh:mm')
        if (self.time.second() % 2) == 0:# эффект мигания двоеточия на часах
            self.txt_clock = self.txt_clock.replace(":", " ")
        self.main_func.ui.Clock.display(self.txt_clock)  
    ###Stutus update connect server function   
    def update_status(self, connected):
        if connected:
            self.main_func.ui.Status_ico.setPixmap(QPixmap(f"qrc/green-square.png"))  # Укажите путь к зеленой картинке
            self.connection_attempts = 0
        else:
            self.main_func.ui.Status_ico.setPixmap(QPixmap(f"qrc/red-square.png"))  # Укажите путь к красной картинке
            self.connection_attempts += 1
            if self.connection_attempts >= 3: #Кол-во попыток переподключения к FTP серверу
                self.ftp_thread.stop()
                self.timer.stop()
    #Проверка подключения к FTP
    def check_connection(self):
        if not self.ftp_thread.isRunning():
            self.ftp_thread.start()
        
