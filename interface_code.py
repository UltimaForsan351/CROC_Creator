
##############################################################################
####Imports lib###
from PySide2 import *
import sys,os
from PySide2.QtWidgets import QStyledItemDelegate
##############################################################################
####Imports Custom Widgets###
from Custom_Widgets import *
##############################################################################
####Imports Fix###
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
##############################################################################
###Import interface file###
from interface_ui import Ui_MainWindow
from usergate_function import *
from menu_function import *
from documents_function import *
from main_function import *
##############################################################################
###Main class###
class MainWindow(QMainWindow): 
    ##############################################################################
    ###Function Class __init###
    def __init__(self): #конструктор класса
        super(MainWindow, self).__init__() #конструктор класса __init__ чтобы пользоваться атрибутами QMainWindo
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UG_creator = Usergate_creator(self)
        self.Menu_functions = Menu_Functions(self)
        self.documents_functions = Documents_Functions(self)
        self.main_functions = Main_Functions(self)
        ##############################################################################
        ###Remove window title bar###
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ##############################################################################
        ###Set main background to transparent###
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ########################################################################
        #json stylesheet
        loadJsonStyle(self, self.ui)
        ########################################################################
        #Default parameters
        self.status_window = 0
        ########################################################################
        ###############################################################################
        ###If left mouse button is clicked###
        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        ##############################################################################
        ###Resize window zone###
        # Создаем QSizeGrip для правого нижнего угла
        QSizeGrip(self.ui.resize_zone)
        ##############################################################################
        ###Click event to move the window###
        self.ui.up.mouseMoveEvent = moveWindow
        ##############################################################################
        ###roll scroll area###
        self.ui.scrollArea.wheelEvent = self.UG_creator.wheelEvent
        self.ui.scrollArea_3.wheelEvent = self.UG_creator.wheelEvent_2
        ##############################################################################
        ###Event clicked on treeView###
        self.ui.treeWidget.itemClicked.connect(self.UG_creator.onItemClicked)
        self.ui.treeWidget.mousePressEvent = self.UG_creator.tree_widget_mouse_press_event
        ##############################################################################
        ###BUTTONS###
        ###resize_window_BTN###
        self.ui.resize_btn.clicked.connect(self.resize_window)
        ###add_Usergates_BTN###
        self.ui.UG_1_add_btn_1.clicked.connect(self.UG_creator.UG_add_C100)
        self.ui.UG_2_add_btn_2.clicked.connect(self.UG_creator.UG_add_C150)
        self.ui.UG_3_add_btn_3.clicked.connect(self.UG_creator.UG_add_D200)
        self.ui.UG_4_add_btn_4.clicked.connect(self.UG_creator.UG_add_D500)
        self.ui.UG_5_add_btn_5.clicked.connect(self.UG_creator.UG_add_E1000)
        self.ui.UG_6_add_btn_6.clicked.connect(self.UG_creator.UG_add_E3000)
        self.ui.UG_7_add_btn_7.clicked.connect(self.UG_creator.UG_add_F8000)
        self.ui.UG_8_add_btn_8.clicked.connect(self.UG_creator.UG_add_X1)
        self.ui.UG_9_add_btn_9.clicked.connect(self.UG_creator.UG_add_FG)
        self.ui.UG_10_add_btn_10.clicked.connect(self.UG_creator.UG_add_VE100)
        self.ui.UG_11_add_btn_11.clicked.connect(self.UG_creator.UG_add_VE200)
        self.ui.UG_12_add_btn_12.clicked.connect(self.UG_creator.UG_add_VE250)
        self.ui.UG_13_add_btn_13.clicked.connect(self.UG_creator.UG_add_VE500)
        self.ui.UG_14_add_btn_14.clicked.connect(self.UG_creator.UG_add_VE2000)
        self.ui.UG_15_add_btn_15.clicked.connect(self.UG_creator.UG_add_VE4000)
        self.ui.UG_16_add_btn_16.clicked.connect(self.UG_creator.UG_add_VE6000)
        ###Remove-string_and_all_BTN###
        self.ui.remove_all_btn.clicked.connect(self.UG_creator.Remove_all)
        self.ui.remove_line_btn.clicked.connect(self.UG_creator.Remove_line)
        ###Download_file_BTN###
        self.ui.download_btn.clicked.connect(self.UG_creator.Download_spec)
        ###add_License_BTN###
        self.ui.ATP_btn.clicked.connect(self.UG_creator.License_add_ATP)
        self.ui.SU_btn.clicked.connect(self.UG_creator.License_add_SU)
        self.ui.Antivirus_btn.clicked.connect(self.UG_creator.License_add_antivirus)
        self.ui.Mail_btn.clicked.connect(self.UG_creator.License_add_Mail)
        self.ui.MGMT_btn.clicked.connect(self.UG_creator.License_add_MGMT)
        self.ui.Log_btn.clicked.connect(self.UG_creator.License_add_Log)
        self.ui.Cluster_btn.clicked.connect(self.UG_creator.License_add_Cluster)
        ###add_card_and_sfp_btn
        self.ui.card_1_btn_1.clicked.connect(self.UG_creator.Сard_8_1)
        self.ui.card_2_btn_2.clicked.connect(self.UG_creator.Сard_4_1)
        self.ui.card_3_btn_3.clicked.connect(self.UG_creator.Сard_4_1_FO)
        self.ui.card_4_btn_4.clicked.connect(self.UG_creator.Сard_4_10)
        self.ui.card_5_btn_5.clicked.connect(self.UG_creator.Сard_4_10_FO)
        self.ui.card_6_btn_6.clicked.connect(self.UG_creator.Сard_1_40)
        self.ui.card_7_btn_7.clicked.connect(self.UG_creator.SFP_RJ_45_1G)
        self.ui.card_8_btn_8.clicked.connect(self.UG_creator.SFP_10G)
        self.ui.card_9_btn_9.clicked.connect(self.UG_creator.SFP_10Gb_500m)
        self.ui.card_10_btn_10.clicked.connect(self.UG_creator.SFP_10Gb_10km)
        self.ui.card_11_btn_11.clicked.connect(self.UG_creator.SFP_SX_1_25)
        self.ui.card_1_btn_1.enterEvent = self.UG_creator.start_timer_Сard_8_1
        self.ui.card_1_btn_1.leaveEvent = self.UG_creator.WINdow_hide_Сard_8_1
        self.ui.card_2_btn_2.enterEvent = self.UG_creator.start_timer_Сard_4_1
        self.ui.card_2_btn_2.leaveEvent = self.UG_creator.WINdow_hide_Сard_4_1
        self.ui.card_3_btn_3.enterEvent = self.UG_creator.start_timer_Сard_4_1_FO
        self.ui.card_3_btn_3.leaveEvent = self.UG_creator.WINdow_hide_Сard_4_1_FO
        self.ui.card_4_btn_4.enterEvent = self.UG_creator.start_timer_Сard_4_10
        self.ui.card_4_btn_4.leaveEvent = self.UG_creator.WINdow_hide_Сard_4_10
        self.ui.card_5_btn_5.enterEvent = self.UG_creator.start_timer_Сard_4_10_FO
        self.ui.card_5_btn_5.leaveEvent = self.UG_creator.WINdow_hide_Сard_4_10_FO
        self.ui.card_6_btn_6.enterEvent = self.UG_creator.start_timer_Сard_1_40
        self.ui.card_6_btn_6.leaveEvent = self.UG_creator.WINdow_hide_Сard_1_40
        self.ui.card_7_btn_7.enterEvent = self.UG_creator.start_timer_SFP_RJ_45_1G
        self.ui.card_7_btn_7.leaveEvent = self.UG_creator.WINdow_hide_SFP_RJ_45_1G
        self.ui.card_8_btn_8.enterEvent = self.UG_creator.start_timer_SFP_10G
        self.ui.card_8_btn_8.leaveEvent = self.UG_creator.WINdow_hide_SFP_10G
        self.ui.card_9_btn_9.enterEvent = self.UG_creator.start_timer_SFP_10Gb_500m
        self.ui.card_9_btn_9.leaveEvent = self.UG_creator.WINdow_hide_SFP_10Gb_500m
        self.ui.card_10_btn_10.enterEvent = self.UG_creator.start_timer_SFP_10Gb_10km
        self.ui.card_10_btn_10.leaveEvent = self.UG_creator.WINdow_hide_SFP_10Gb_10km
        self.ui.card_11_btn_11.enterEvent = self.UG_creator.start_timer_SFP_SX_1_25
        self.ui.card_11_btn_11.leaveEvent = self.UG_creator.WINdow_hide_SFP_SX_1_25
        ###checkBox btn
        self.ui.check_yes.stateChanged.connect(self.UG_creator.on_check_yes_changed)
        self.ui.check_no.stateChanged.connect(self.UG_creator.on_check_no_changed)
        self.ui.standart_checkBox.stateChanged.connect(self.UG_creator.standart_changed)
        self.ui.premium_checkBox.stateChanged.connect(self.UG_creator.premium_changed)
        ###Spinbox btn
        self.ui.yearBox.valueChanged.connect(self.UG_creator.spinbox_yearBox_changed)
        self.ui.yearBox_tp.valueChanged.connect(self.UG_creator.spinbox_yearBox_tp_changed)
        ###text comment btn
        self.ui.comentEdit.textChanged.connect(self.UG_creator.on_text_coment_changed)
        ###Menu edit image btn
        self.ui.openMenu_btn.clicked.connect(self.Menu_functions.resize_Menu_left)
        ###Menu btn
        self.ui.MainFunction_btn.clicked.connect(lambda: self.Menu_functions.change_page(0))
        self.ui.Usergate_btn.clicked.connect(lambda: self.Menu_functions.change_page(1))
        self.ui.Documents_btn.clicked.connect(lambda: self.Menu_functions.change_page(2))
        
        ##############################################################################
        ###Show Window###
        self.show()    
    ##############################################################################
    ###resize window event###
    def resize_window(self):
            if self.status_window == 0: 
                self.status_window = 1
                self.showFullScreen()
            else:
                self.status_window = 0
                self.showNormal()
    ##############################################################################
    ###Add mouse events to the window###
    def mousePressEvent (self, event):
        self.clickPosition = event.globalPos() #get current position of the mouse
##############################################################################
###Execute app###
if __name__ == "__main__":
    app_main = QApplication(sys.argv) #создание потока для приложения
    window_main=MainWindow() 
    sys.exit(app_main.exec_()) #завершение потока
