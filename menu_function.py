##############################################################################
####Imports lib###
from PySide2 import QtCore, QtWidgets, QtGui
import sys,os
##############################################################################
###Import interface file###
from interface_ui import *
from Custom_Widgets import *
#MAIN init  
class Menu_Functions(QMainWindow):
    def __init__(self, object):
        QMainWindow.__init__(self)
        self.menu_func = object
    #инициализация текущей странички
        self.current_page = 0
        self.update_button_colors()
    #инициализация текущей картинки
        self.image_menu_left = 0
    #Change page    
    def change_page(self, index):
        self.menu_func.ui.stackedWidget.setCurrentIndex(index)
        self.current_page = index
        self.update_button_colors()
    #Change update collors
    def update_button_colors(self):
        # Сбрасываем цвет всех кнопок
        self.menu_func.ui.MainFunction_btn.setStyleSheet("")
        self.menu_func.ui.Usergate_btn.setStyleSheet("")
        self.menu_func.ui.Documents_btn.setStyleSheet("")
        # Подсвечиваем текущую кнопку
        if self.current_page == 0:
            self.menu_func.ui.MainFunction_btn.setStyleSheet("background-color: rgb(32, 47, 52)")
        elif self.current_page == 1:
            self.menu_func.ui.Usergate_btn.setStyleSheet("background-color: rgb(32, 47, 52)")
        elif self.current_page == 2:
            self.menu_func.ui.Documents_btn.setStyleSheet("background-color: rgb(32, 47, 52)")
    ##############################################################################
    ###Resize_menu edit image### 
    def resize_Menu_left(self):
        if self.image_menu_left == 0:           
            self.menu_func.ui.openMenu_btn.setIcon(QIcon(r"qrc/arrowhead-thin-outline-to-the-left.png"))
            self.image_menu_left = 1
        else:
            self.menu_func.ui.openMenu_btn.setIcon(QIcon(r"qrc/right-arrow.png"))
            self.image_menu_left = 0     