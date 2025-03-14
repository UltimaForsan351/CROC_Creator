# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

import interface_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.Stilesheet = QWidget(MainWindow)
        self.Stilesheet.setObjectName(u"Stilesheet")
        self.Stilesheet.setMinimumSize(QSize(0, 0))
        self.Stilesheet.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.Stilesheet.setFont(font)
        self.Stilesheet.setStyleSheet(u" /*  Menu BG */\n"
"#main {\n"
"}\n"
"#Bg_status_FTP{\n"
"	background-color: rgb(32, 47, 52);\n"
"	border-radius: 5px;\n"
"}\n"
"#mainR {	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#up {	\n"
"	background-color: rgb(13, 18, 22);\n"
"}\n"
"\n"
"#down {	\n"
"	background-color: rgb(13, 18, 22);\n"
"}\n"
"\n"
"#slide {	\n"
"	background-color: rgb(13, 18, 22);\n"
"}\n"
"\n"
"#slide_button {	\n"
"	background-color: rgb(13, 18, 22);\n"
"}\n"
"\n"
"#main_stacked{	\n"
"	background-color: rgb(32, 47, 52);\n"
"}\n"
"\n"
"#Clock, #FTP_status_text{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#page_1, #page_2, #page_3, #page_4, #page_5, #page_6, #page_7, #page_8, #page_9, #page_10 {	\n"
"	background-color: rgb(20, 31, 37);\n"
"}\n"
"\n"
"#scrollA, #scrollArea,#scrollB, #scrollArea_2, #scrollC, #scrollArea_3, #scrollArea_4, #scrollD, #scrollArea_5, #scrollE  {\n"
"	background-color: rgb(20, 31, 37);\n"
"	border: none;\n"
"}\n"
"#slide_glow_1, #slide_glow_2, #slide_glow_3, #slide_glow_4,#slide_glow_5, #slide"
                        "_glow_6, #slide_glow_7, #slide_glow_8, #slide_glow_9, #slide_glow_10 {	\n"
"	background-color: rgb(170, 255, 0);\n"
"}\n"
"#bg_glow_1, #bg_glow_2, #bg_glow_3, #bg_glow_4, #bg_glow_5, #bg_glow_6, #bg_glow_7, #bg_glow_8, #bg_glow_9, #bg_glow_10 {	\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" /*  UG Creator */\n"
"\n"
"#UG_yes, #UG_no, #year_name, #year_name_3, #standart, #premium {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#card_1_bg_1, #card_2_bg_2,#card_3_bg_3, #card_4_bg_4, #card_5_bg_5, #card_6_bg_6, #card_7_bg_7, #card_8_bg_8, #card_9_bg_9, #card_10_bg_10, #card_11_bg_11{\n"
"	border-radius: 20px;\n"
"	background-color: rgba(87, 94, 107, 255);\n"
"	border:1px solid rgb(13, 18, 22)\n"
"}\n"
"#UG_1, #UG_2, #UG_3, #UG_4, #UG_5, #UG_6, #UG_7, #UG_8, #UG_9, #UG_10, #UG_11, #UG_12, #UG_13, #UG_14, #UG_15, #UG_16 {	\n"
"	border-radius: 15px;\n"
"	background-color: rgba(87, 94, 107, 100);\n"
"}\n"
"#UG_1_logo_1, #UG_2_logo_2, #UG_3_logo_3, #UG_4_logo_4, #UG_5_logo_5, #UG_6_logo_"
                        "6, #UG_7_logo_7, #UG_8_logo_8, #UG_9_logo_9, #UG_10_logo_10, #UG_11_logo_11, #UG_12_logo_12, #UG_13_logo_13, #UG_14_logo_14, #UG_15_logo_15, #UG_16_logo_16, #card_1_logo_1, #card_2_logo_2, #card_3_logo_3, #card_4_logo_4, #card_5_logo_5, #card_6_logo_6, #card_7_logo_7, #card_8_logo_8, #card_9_logo_9, #card_10_logo_10, #card_11_logo_11{	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#UG_1_BG_1, #UG_2_BG_2, #UG_3_BG_3, #UG_4_BG_4, #UG_5_BG_5, #UG_6_BG_6, #UG_7_BG_7, #UG_8_BG_8, #UG_9_BG_9, #UG_10_BG_10, #UG_11_BG_11, #UG_12_BG_12, #UG_13_BG_13, #UG_14_BG_14, #UG_15_BG_15, #UG_16_BG_16 {	\n"
"	background-color: rgba(20, 31, 37, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton#UG_1_add_btn_1, QPushButton#UG_2_add_btn_2, QPushButton#UG_3_add_btn_3, QPushButton#UG_4_add_btn_4, QPushButton#UG_5_add_btn_5, QPushButton#UG_6_add_btn_6, QPushButton#UG_7_add_btn_7, QPushButton#UG_8_add_btn_8, QPushButton#UG_9_add_btn_9, QPushButton#UG_10_add_btn_10, QPushButton#UG_11_add_btn_11, QPushButton#UG_12_add_btn_12, QPushButton#U"
                        "G_13_add_btn_13, QPushButton#UG_14_add_btn_14, QPushButton#UG_15_add_btn_15, QPushButton#UG_16_add_btn_16{\n"
"	background-color: rgb(13, 18, 22);\n"
"	border:2px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#UG_1_add_btn_1:hover, QPushButton#UG_2_add_btn_2:hover, QPushButton#UG_3_add_btn_3:hover, QPushButton#UG_4_add_btn_4:hover, QPushButton#UG_5_add_btn_5:hover, QPushButton#UG_6_add_btn_6:hover, QPushButton#UG_7_add_btn_7:hover, QPushButton#UG_8_add_btn_8:hover, QPushButton#UG_9_add_btn_9:hover, QPushButton#UG_10_add_btn_10:hover, QPushButton#UG_11_add_btn_11:hover, QPushButton#UG_12_add_btn_12:hover, QPushButton#UG_13_add_btn_13:hover, QPushButton#UG_14_add_btn_14:hover, QPushButton#UG_15_add_btn_15:hover, QPushButton#UG_16_add_btn_16:hover{ \n"
"	padding-bottom: 2px;\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: rgb(13, 18, 22);\n"
"}\n"
"QPushButton#UG_1_add_btn_1:pressed, QPushButton#UG_2_add_btn_2:pressed, QPushButton#UG_3_add_btn_3"
                        ":pressed, QPushButton#UG_4_add_btn_4:pressed, QPushButton#UG_5_add_btn_5:pressed, QPushButton#UG_6_add_btn_6:pressed, QPushButton#UG_7_add_btn_7:pressed, QPushButton#UG_8_add_btn_8:pressed, QPushButton#UG_9_add_btn_9:pressed, QPushButton#UG_10_add_btn_10:pressed, QPushButton#UG_11_add_btn_11:pressed, QPushButton#UG_12_add_btn_12:pressed, QPushButton#UG_13_add_btn_13:pressed, QPushButton#UG_14_add_btn_14:pressed, QPushButton#UG_15_add_btn_15:pressed, QPushButton#UG_16_add_btn_16:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"	background-color: rgb(170, 255, 0);\n"
"	color: rgb(13, 18, 22);\n"
"}\n"
"QPushButton#SU_btn, QPushButton#ATP_btn, QPushButton#Antivirus_btn, QPushButton#Log_btn, QPushButton#MGMT_btn, QPushButton#Mail_btn, QPushButton#Cluster_btn{\n"
"	background-color: rgb(13, 18, 22);\n"
"	border:1px solid rgba(255, 255, 255, 255);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#SU_btn:hover, QPushButton#ATP_btn:hover, QPushButton#Antivirus_btn:hover, QPushB"
                        "utton#Log_btn:hover, QPushButton#MGMT_btn:hover, QPushButton#Mail_btn:hover, QPushButton#Cluster_btn:hover{ \n"
"	background-color: rgb(255, 170, 0);\n"
"	padding-bottom: 2px;\n"
"	color: rgb(13, 18, 22);\n"
"}\n"
"QPushButton#SU_btn:pressed, QPushButton#ATP_btn:pressed, QPushButton#Antivirus_btn:pressed, QPushButton#Log_btn:pressed, QPushButton#MGMT_btn:pressed, QPushButton#Mail_btn:pressed, QPushButton#Cluster_btn:pressed{\n"
"	background-color: rgb(170, 255, 0);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"	color: rgb(13, 18, 22);\n"
"}\n"
"#Licensing_logo, #Network_cards_logo, #FSTEC_logo, #Moduls_data_logo, #TP_logo, #Comments_logo {	\n"
"	border-radius: 15px;\n"
"	background-color: rgb(12, 17, 20);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#File_name_logo{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#File_name_edit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(12, 17, 20);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#remove_line_btn{\n"
"	color: rgb(13, 18, 22);\n"
"	background-c"
                        "olor: rgb(255, 170, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#remove_line_btn:hover{\n"
"	background-color: rgb(255, 140, 0); \n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#remove_line_btn:pressed{\n"
"	background-color: rgb(170, 0, 0);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px\n"
"}\n"
"QPushButton#remove_all_btn{\n"
"	color: rgb(13, 18, 22);\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#remove_all_btn:hover{\n"
"	background-color: rgb(255, 140, 0); \n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#remove_all_btn:pressed{\n"
"	background-color: rgb(170, 0, 0);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px\n"
"}\n"
"\n"
"QPushButton#card_1_btn_1, QPushButton#card_2_btn_2, QPushButton#card_3_btn_3, QPushButton#card_4_btn_4, QPushButton#card_5_btn_5, QPushButton#card_6_btn_6, QPushButton#card_7_btn_7, QPushButton#card_8_btn_8, QPushButton#card_9_btn_9, QPushButton#card_10_btn_10, QPushButton#card_11_btn_11{\n"
"	background-color: rgb(87, 94, 107);\n"
"	bord"
                        "er-radius: 20px;\n"
"}\n"
"QPushButton#card_1_btn_1:hover, QPushButton#card_2_btn_2:hover, QPushButton#card_3_btn_3:hover, QPushButton#card_4_btn_4:hover, QPushButton#card_5_btn_5:hover, QPushButton#card_6_btn_6:hover, QPushButton#card_7_btn_7:hover, QPushButton#card_8_btn_8:hover, QPushButton#card_9_btn_9:hover, QPushButton#card_10_btn_10:hover, QPushButton#card_11_btn_11:hover{\n"
"	background-color: rgb(255, 170, 0); \n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#card_1_btn_1:pressed, QPushButton#card_2_btn_2:pressed, QPushButton#card_3_btn_3:pressed, QPushButton#card_4_btn_4:pressed, QPushButton#card_5_btn_5:pressed, QPushButton#card_6_btn_6:pressed, QPushButton#card_7_btn_7:pressed, QPushButton#card_8_btn_8:pressed, QPushButton#card_9_btn_9:pressed, QPushButton#card_10_btn_10:pressed, QPushButton#card_11_btn_11:pressed {\n"
"	background-color: rgb(170, 255, 0);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* Clouse - resize - roll  BTN*/\n"
"\n"
"\n"
"QPushButton#clouse_bt"
                        "n{\n"
"	border: none;\n"
"}\n"
"QPushButton#clouse_btn:hover{ \n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#clouse_btn:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"QPushButton#roll_btn{\n"
"	border: none;\n"
"}\n"
"QPushButton#roll_btn:hover{\n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#roll_btn:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"QPushButton#resize_btn{\n"
"	border: none;\n"
"}\n"
"QPushButton#resize_btn:hover{\n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#resize_btn:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton#openMenu_btn{\n"
"	border: none;\n"
"}\n"
"QPushButton#openMenu_btn:hover{\n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#openMenu_btn:pressed{\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"QPushButton#Usergate_btn, QPushButton#MainFunction_btn, QPushButton#Documents_btn{\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgba(200, 200, 200, 255);\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
""
                        "QPushButton#Usergate_btn:hover, QPushButton#MainFunction_btn:hover, QPushButton#Documents_btn:hover{\n"
"	padding-bottom: 2px;\n"
"	background-color: rgb(18, 32, 35);\n"
"}\n"
"QPushButton#Usergate_btn:pressed, QPushButton#MainFunction_btn:pressed, QPushButton#Documents_btn:pressed{\n"
"	background-color: rgb(44, 44, 44);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"QPushButton#download_btn{\n"
"	color: rgb(13, 18, 22);\n"
"	background-color: rgb(170, 255, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#download_btn:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"	padding-bottom: 4px;\n"
"}\n"
"QPushButton#download_btn:pressed{\n"
"	background-color: rgb(255, 140, 0);\n"
"	padding-left: 3px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"\n"
"/*  VERTICAL SCROLLBAR  UG */\n"
"\n"
"\n"
"QScrollBar:horizontal{\n"
"	background-color: rgb(87, 94, 107);\n"
"	height: 5px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	background-color: rgb(87, 94, 107);\n"
"	width: 5px;\n"
"	border-radius: "
                        "3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(170, 255, 0);\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{	\n"
"	background-color: rgb(255, 140, 0);\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(170, 255, 0);\n"
"	min-height: 30px;\n"
"	border-radius: 2px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{	\n"
"	background-color: rgb(255, 140, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgba(87, 94, 107,100);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	ba"
                        "ckground-color: rgba(87, 94, 107,100);\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	border:none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	border:none;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"QTreeWidget {\n"
"	background-color: rgb(13, 18, 22);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 12px;\n"
"	border-radius: 3px;\n"
"	outline: none;\n"
"}\n"
"QTreeWidget::item {\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 3px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"QTreeWidget::item:hover {\n"
"	color: rgb(255, 255, 255);         \n"
"	background-color: rgba(87, 94, 107, 100);\n"
"	border-radius: 3px;\n"
"}\n"
"QTreeWidget::item:selected {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(170, 255, 0, 100);\n"
"	border:none;\n"
"}\n"
"\n"
"QTextEdit{\n"
""
                        "	border-radius: 15px;\n"
"	background-color: rgb(13, 18, 22);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius:8px;\n"
"	border: 2px solid gray;\n"
"	background-color: rgb(13, 18, 22);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(170, 255, 0);\n"
"	border: 2px solid gray;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	background-color: rgb(13, 18, 22);\n"
"	color: white;\n"
"	border: 1px solid gray;\n"
"	border-radius: 4px;\n"
"	padding: 2px;\n"
"}\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-radius: 4px;\n"
"	width: 18px;\n"
"	height: 9px;\n"
"}\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"	background-color: rgb(255, 140, 0);\n"
"}\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"	width: 5px;\n"
"	height: 5px;\n"
"}\n"
"\n"
"\n"
"/* Main Functions*/\n"
"#progressBar_download{\n"
"	color: rgb(0, 170, 0);\n"
"	border-radius: 7px;\n"
"	background-color"
                        ": rgb(13, 18, 22);\n"
"}\n"
"#progressBar_download::chunk{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(170, 255, 0);\n"
"}\n"
"#Block_1, #Block_2, #Block_3, #Block_4, #Block_5, #Block_6, #Block_7, #Block_8, #Block_9, #Block_10{\n"
"	border-radius: 13px;\n"
"	background-color: rgba(87, 94, 107, 255);\n"
"	border:1px solid rgb(13, 18, 22)\n"
"}\n"
"#Block_1_up_1, #Block_2_up_2, #Block_3_up_3{\n"
"	background-color: rgba(0, 0, 0, 150);\n"
"	border-bottom-left-radius:11px;\n"
"	border-bottom-right-radius:11px;\n"
"	border-top-left-radius:14px;\n"
"	border-top-right-radius:14px;\n"
"}\n"
"#FTP_connections_logo{\n"
"	border-radius: 11px;\n"
"	border-bottom: 2px solid rgba(200, 200, 200, 255);\n"
"	color:rgb(255, 255, 255);\n"
"	\n"
"}")
        self.horizontalLayout_23 = QHBoxLayout(self.Stilesheet)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.main = QWidget(self.Stilesheet)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 0))
        self.main.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide = QCustomSlideMenu(self.main)
        self.slide.setObjectName(u"slide")
        self.slide.setMinimumSize(QSize(0, 0))
        self.slide.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.slide)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.bg = QWidget(self.slide)
        self.bg.setObjectName(u"bg")
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.bg)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 20))
        self.widget.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.w_1 = QWidget(self.widget_3)
        self.w_1.setObjectName(u"w_1")
        self.w_1.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.w_1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bg_glow_1 = QWidget(self.w_1)
        self.bg_glow_1.setObjectName(u"bg_glow_1")
        self.bg_glow_1.setMinimumSize(QSize(0, 2))
        self.bg_glow_1.setMaximumSize(QSize(16777215, 2))
        self.verticalLayout_7 = QVBoxLayout(self.bg_glow_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.slide_glow_1 = QCustomSlideMenu(self.bg_glow_1)
        self.slide_glow_1.setObjectName(u"slide_glow_1")
        self.slide_glow_1.setMaximumSize(QSize(0, 16777215))
        self.gridLayout_3 = QGridLayout(self.slide_glow_1)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.slide_glow_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.slide_glow_1)


        self.verticalLayout_9.addWidget(self.bg_glow_1)

        self.w_bottom_1 = QWidget(self.w_1)
        self.w_bottom_1.setObjectName(u"w_bottom_1")
        self.verticalLayout_8 = QVBoxLayout(self.w_bottom_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 12)
        self.MainFunction_btn = QPushButton(self.w_bottom_1)
        self.MainFunction_btn.setObjectName(u"MainFunction_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainFunction_btn.sizePolicy().hasHeightForWidth())
        self.MainFunction_btn.setSizePolicy(sizePolicy1)
        self.MainFunction_btn.setMinimumSize(QSize(191, 42))
        font1 = QFont()
        font1.setFamily(u"Bookman Old Style")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.MainFunction_btn.setFont(font1)
        self.MainFunction_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.MainFunction_btn)


        self.verticalLayout_9.addWidget(self.w_bottom_1)


        self.verticalLayout_3.addWidget(self.w_1)

        self.w_2 = QWidget(self.widget_3)
        self.w_2.setObjectName(u"w_2")
        self.verticalLayout_4 = QVBoxLayout(self.w_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bg_glow_2 = QWidget(self.w_2)
        self.bg_glow_2.setObjectName(u"bg_glow_2")
        self.bg_glow_2.setMinimumSize(QSize(0, 2))
        self.bg_glow_2.setMaximumSize(QSize(16777215, 2))
        self.verticalLayout_5 = QVBoxLayout(self.bg_glow_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.slide_glow_2 = QCustomSlideMenu(self.bg_glow_2)
        self.slide_glow_2.setObjectName(u"slide_glow_2")
        self.slide_glow_2.setMinimumSize(QSize(0, 0))
        self.slide_glow_2.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_87 = QVBoxLayout(self.slide_glow_2)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.slide_glow_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_87.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.slide_glow_2)


        self.verticalLayout_4.addWidget(self.bg_glow_2)

        self.w_bottom_2 = QWidget(self.w_2)
        self.w_bottom_2.setObjectName(u"w_bottom_2")
        self.verticalLayout_6 = QVBoxLayout(self.w_bottom_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 12)
        self.Usergate_btn = QPushButton(self.w_bottom_2)
        self.Usergate_btn.setObjectName(u"Usergate_btn")
        sizePolicy1.setHeightForWidth(self.Usergate_btn.sizePolicy().hasHeightForWidth())
        self.Usergate_btn.setSizePolicy(sizePolicy1)
        self.Usergate_btn.setMinimumSize(QSize(191, 42))
        self.Usergate_btn.setFont(font1)
        self.Usergate_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Usergate_btn.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.Usergate_btn)


        self.verticalLayout_4.addWidget(self.w_bottom_2)


        self.verticalLayout_3.addWidget(self.w_2)

        self.w_3 = QWidget(self.widget_3)
        self.w_3.setObjectName(u"w_3")

        self.verticalLayout_3.addWidget(self.w_3)

        self.w_4 = QWidget(self.widget_3)
        self.w_4.setObjectName(u"w_4")

        self.verticalLayout_3.addWidget(self.w_4)

        self.w_5 = QWidget(self.widget_3)
        self.w_5.setObjectName(u"w_5")
        self.verticalLayout_15 = QVBoxLayout(self.w_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer = QSpacerItem(20, 298, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.w_5)

        self.w_6 = QWidget(self.widget_3)
        self.w_6.setObjectName(u"w_6")

        self.verticalLayout_3.addWidget(self.w_6)

        self.w_7 = QWidget(self.widget_3)
        self.w_7.setObjectName(u"w_7")

        self.verticalLayout_3.addWidget(self.w_7)

        self.w_8 = QWidget(self.widget_3)
        self.w_8.setObjectName(u"w_8")

        self.verticalLayout_3.addWidget(self.w_8)

        self.w_9 = QWidget(self.widget_3)
        self.w_9.setObjectName(u"w_9")

        self.verticalLayout_3.addWidget(self.w_9)

        self.w_10 = QWidget(self.widget_3)
        self.w_10.setObjectName(u"w_10")
        self.verticalLayout_12 = QVBoxLayout(self.w_10)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bg_glow_3 = QWidget(self.w_10)
        self.bg_glow_3.setObjectName(u"bg_glow_3")
        self.bg_glow_3.setMinimumSize(QSize(0, 2))
        self.bg_glow_3.setMaximumSize(QSize(16777215, 2))
        self.verticalLayout_10 = QVBoxLayout(self.bg_glow_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.slide_glow_10 = QCustomSlideMenu(self.bg_glow_3)
        self.slide_glow_10.setObjectName(u"slide_glow_10")
        self.slide_glow_10.setMaximumSize(QSize(0, 16777215))
        self.gridLayout_4 = QGridLayout(self.slide_glow_10)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.slide_glow_10)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_10, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.slide_glow_10)


        self.verticalLayout_12.addWidget(self.bg_glow_3)

        self.w_bottom_3 = QWidget(self.w_10)
        self.w_bottom_3.setObjectName(u"w_bottom_3")
        self.verticalLayout_11 = QVBoxLayout(self.w_bottom_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 12)
        self.Documents_btn = QPushButton(self.w_bottom_3)
        self.Documents_btn.setObjectName(u"Documents_btn")
        sizePolicy1.setHeightForWidth(self.Documents_btn.sizePolicy().hasHeightForWidth())
        self.Documents_btn.setSizePolicy(sizePolicy1)
        self.Documents_btn.setMinimumSize(QSize(191, 42))
        self.Documents_btn.setFont(font1)
        self.Documents_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.Documents_btn)


        self.verticalLayout_12.addWidget(self.w_bottom_3)


        self.verticalLayout_3.addWidget(self.w_10)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.bg)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 15))
        self.widget_4.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.bg)


        self.horizontalLayout.addWidget(self.slide)

        self.mainR = QWidget(self.main)
        self.mainR.setObjectName(u"mainR")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainR.sizePolicy().hasHeightForWidth())
        self.mainR.setSizePolicy(sizePolicy2)
        self.mainR.setMinimumSize(QSize(0, 0))
        self.mainR.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.mainR)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.up = QWidget(self.mainR)
        self.up.setObjectName(u"up")
        self.up.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.up)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.up)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.widget_91 = QWidget(self.widget_2)
        self.widget_91.setObjectName(u"widget_91")

        self.horizontalLayout_55.addWidget(self.widget_91)

        self.widget_92 = QWidget(self.widget_2)
        self.widget_92.setObjectName(u"widget_92")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.widget_93 = QWidget(self.widget_92)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMinimumSize(QSize(150, 0))
        self.widget_93.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_70 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(-1, 0, 0, 0)
        self.widget_95 = QWidget(self.widget_93)
        self.widget_95.setObjectName(u"widget_95")

        self.horizontalLayout_70.addWidget(self.widget_95)

        self.widget_96 = QWidget(self.widget_93)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMinimumSize(QSize(150, 0))
        self.widget_96.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_91 = QVBoxLayout(self.widget_96)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(3, 3, 3, 2)
        self.Bg_status_FTP = QWidget(self.widget_96)
        self.Bg_status_FTP.setObjectName(u"Bg_status_FTP")
        self.horizontalLayout_71 = QHBoxLayout(self.Bg_status_FTP)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.Bg_status_FTP_text = QWidget(self.Bg_status_FTP)
        self.Bg_status_FTP_text.setObjectName(u"Bg_status_FTP_text")
        self.verticalLayout_92 = QVBoxLayout(self.Bg_status_FTP_text)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 1)
        self.FTP_status_text = QLabel(self.Bg_status_FTP_text)
        self.FTP_status_text.setObjectName(u"FTP_status_text")
        font2 = QFont()
        font2.setFamily(u"Bookman Old Style")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.FTP_status_text.setFont(font2)
        self.FTP_status_text.setScaledContents(False)
        self.FTP_status_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.FTP_status_text)


        self.horizontalLayout_71.addWidget(self.Bg_status_FTP_text)

        self.Bg_status_FTP_ico = QWidget(self.Bg_status_FTP)
        self.Bg_status_FTP_ico.setObjectName(u"Bg_status_FTP_ico")
        self.Bg_status_FTP_ico.setMaximumSize(QSize(30, 16777215))
        self.horizontalLayout_88 = QHBoxLayout(self.Bg_status_FTP_ico)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(5, 0, 5, 0)
        self.Status_ico = QLabel(self.Bg_status_FTP_ico)
        self.Status_ico.setObjectName(u"Status_ico")
        self.Status_ico.setPixmap(QPixmap(u":/ico/red-square.png"))
        self.Status_ico.setScaledContents(True)

        self.horizontalLayout_88.addWidget(self.Status_ico)


        self.horizontalLayout_71.addWidget(self.Bg_status_FTP_ico)


        self.verticalLayout_91.addWidget(self.Bg_status_FTP)


        self.horizontalLayout_70.addWidget(self.widget_96)


        self.horizontalLayout_56.addWidget(self.widget_93)

        self.widget_94 = QWidget(self.widget_92)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setMinimumSize(QSize(100, 0))
        self.widget_94.setMaximumSize(QSize(100, 16777215))
        self.gridLayout = QGridLayout(self.widget_94)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 1, 0, 1)
        self.Clock = QLCDNumber(self.widget_94)
        self.Clock.setObjectName(u"Clock")
        font3 = QFont()
        font3.setFamily(u"Bookman Old Style")
        font3.setPointSize(10)
        self.Clock.setFont(font3)
        self.Clock.setLayoutDirection(Qt.LeftToRight)
        self.Clock.setFrameShape(QFrame.NoFrame)
        self.Clock.setLineWidth(0)
        self.Clock.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.Clock, 0, 0, 1, 1)


        self.horizontalLayout_56.addWidget(self.widget_94)


        self.horizontalLayout_55.addWidget(self.widget_92)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.button_resize = QWidget(self.up)
        self.button_resize.setObjectName(u"button_resize")
        self.button_resize.setMinimumSize(QSize(0, 0))
        self.button_resize.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.button_resize)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.roll_btn = QPushButton(self.button_resize)
        self.roll_btn.setObjectName(u"roll_btn")
        self.roll_btn.setMinimumSize(QSize(24, 21))
        self.roll_btn.setMaximumSize(QSize(24, 21))
        self.roll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.roll_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/ico/circle_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.roll_btn.setIcon(icon)
        self.roll_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_5.addWidget(self.roll_btn)

        self.resize_btn = QPushButton(self.button_resize)
        self.resize_btn.setObjectName(u"resize_btn")
        self.resize_btn.setMinimumSize(QSize(24, 21))
        self.resize_btn.setMaximumSize(QSize(24, 21))
        self.resize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.resize_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/ico/circle_yellow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_btn.setIcon(icon1)
        self.resize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_5.addWidget(self.resize_btn)

        self.clouse_btn = QPushButton(self.button_resize)
        self.clouse_btn.setObjectName(u"clouse_btn")
        self.clouse_btn.setMinimumSize(QSize(24, 21))
        self.clouse_btn.setMaximumSize(QSize(24, 21))
        self.clouse_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clouse_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/ico/circle_red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clouse_btn.setIcon(icon2)
        self.clouse_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_5.addWidget(self.clouse_btn)


        self.horizontalLayout_4.addWidget(self.button_resize)


        self.verticalLayout.addWidget(self.up)

        self.mid = QWidget(self.mainR)
        self.mid.setObjectName(u"mid")
        self.horizontalLayout_3 = QHBoxLayout(self.mid)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slide_button = QWidget(self.mid)
        self.slide_button.setObjectName(u"slide_button")
        self.slide_button.setMinimumSize(QSize(20, 0))
        self.slide_button.setMaximumSize(QSize(20, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.slide_button)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.openMenu_btn = QPushButton(self.slide_button)
        self.openMenu_btn.setObjectName(u"openMenu_btn")
        self.openMenu_btn.setMinimumSize(QSize(24, 24))
        self.openMenu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/ico/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openMenu_btn.setIcon(icon3)
        self.openMenu_btn.setIconSize(QSize(16, 16))
        self.openMenu_btn.setAutoRepeat(False)
        self.openMenu_btn.setAutoRepeatDelay(300)
        self.openMenu_btn.setAutoRepeatInterval(100)

        self.horizontalLayout_7.addWidget(self.openMenu_btn)


        self.horizontalLayout_3.addWidget(self.slide_button)

        self.main_stacked = QWidget(self.mid)
        self.main_stacked.setObjectName(u"main_stacked")
        self.horizontalLayout_6 = QHBoxLayout(self.main_stacked)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.main_stacked)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_105 = QVBoxLayout(self.page_1)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.page_1)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollD = QWidget()
        self.scrollD.setObjectName(u"scrollD")
        self.scrollD.setGeometry(QRect(0, 0, 947, 1000))
        self.horizontalLayout_91 = QHBoxLayout(self.scrollD)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.SizeD = QWidget(self.scrollD)
        self.SizeD.setObjectName(u"SizeD")
        self.verticalLayout_106 = QVBoxLayout(self.SizeD)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.widget_101 = QWidget(self.SizeD)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setMinimumSize(QSize(0, 250))
        self.widget_101.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_92 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_92.setSpacing(5)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(3, 2, 3, 3)
        self.Block_1 = QWidget(self.widget_101)
        self.Block_1.setObjectName(u"Block_1")
        self.verticalLayout_114 = QVBoxLayout(self.Block_1)
        self.verticalLayout_114.setSpacing(0)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.Block_1_up_1 = QWidget(self.Block_1)
        self.Block_1_up_1.setObjectName(u"Block_1_up_1")
        self.Block_1_up_1.setMinimumSize(QSize(0, 25))
        self.Block_1_up_1.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_95 = QHBoxLayout(self.Block_1_up_1)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.FTP_connections_logo = QLabel(self.Block_1_up_1)
        self.FTP_connections_logo.setObjectName(u"FTP_connections_logo")
        font4 = QFont()
        font4.setFamily(u"Bookman Old Style")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.FTP_connections_logo.setFont(font4)
        self.FTP_connections_logo.setScaledContents(False)
        self.FTP_connections_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_95.addWidget(self.FTP_connections_logo)


        self.verticalLayout_114.addWidget(self.Block_1_up_1)

        self.widget_106 = QWidget(self.Block_1)
        self.widget_106.setObjectName(u"widget_106")

        self.verticalLayout_114.addWidget(self.widget_106)


        self.horizontalLayout_92.addWidget(self.Block_1)

        self.Block_2 = QWidget(self.widget_101)
        self.Block_2.setObjectName(u"Block_2")

        self.horizontalLayout_92.addWidget(self.Block_2)

        self.Block_3 = QWidget(self.widget_101)
        self.Block_3.setObjectName(u"Block_3")

        self.horizontalLayout_92.addWidget(self.Block_3)


        self.verticalLayout_106.addWidget(self.widget_101)

        self.widget_104 = QWidget(self.SizeD)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setMinimumSize(QSize(0, 250))
        self.widget_104.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_93 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_93.setSpacing(5)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(3, 2, 3, 3)
        self.Block_4 = QWidget(self.widget_104)
        self.Block_4.setObjectName(u"Block_4")

        self.horizontalLayout_93.addWidget(self.Block_4)

        self.Block_5 = QWidget(self.widget_104)
        self.Block_5.setObjectName(u"Block_5")

        self.horizontalLayout_93.addWidget(self.Block_5)

        self.Block_6 = QWidget(self.widget_104)
        self.Block_6.setObjectName(u"Block_6")

        self.horizontalLayout_93.addWidget(self.Block_6)


        self.verticalLayout_106.addWidget(self.widget_104)

        self.widget_102 = QWidget(self.SizeD)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMinimumSize(QSize(0, 250))
        self.widget_102.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout_106.addWidget(self.widget_102)

        self.widget_103 = QWidget(self.SizeD)
        self.widget_103.setObjectName(u"widget_103")
        self.widget_103.setMinimumSize(QSize(0, 250))
        self.widget_103.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout_106.addWidget(self.widget_103)


        self.horizontalLayout_91.addWidget(self.SizeD)

        self.scrollArea_4.setWidget(self.scrollD)

        self.verticalLayout_105.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_14 = QVBoxLayout(self.widget_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(315, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_8.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 5, 0)
        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.download_btn = QPushButton(self.widget_9)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setMinimumSize(QSize(100, 25))
        self.download_btn.setFont(font2)
        self.download_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.download_btn)


        self.horizontalLayout_8.addWidget(self.widget_9)


        self.verticalLayout_13.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.widget_6.setMaximumSize(QSize(16777215, 120))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 4, 0, 0)
        self.scrollArea = QScrollArea(self.widget_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollA = QWidget()
        self.scrollA.setObjectName(u"scrollA")
        self.scrollA.setGeometry(QRect(0, 0, 2479, 111))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollA)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.SizeA = QWidget(self.scrollA)
        self.SizeA.setObjectName(u"SizeA")
        self.SizeA.setMinimumSize(QSize(0, 0))
        self.SizeA.setMaximumSize(QSize(3000, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.SizeA)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 3, 2, 3)
        self.UG_1 = QWidget(self.SizeA)
        self.UG_1.setObjectName(u"UG_1")
        self.UG_1.setMinimumSize(QSize(150, 0))
        self.UG_1.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.UG_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 0, 2, 0)
        self.widget_11 = QWidget(self.UG_1)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_17 = QVBoxLayout(self.widget_11)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.UG_1_logo_1 = QLabel(self.widget_11)
        self.UG_1_logo_1.setObjectName(u"UG_1_logo_1")
        self.UG_1_logo_1.setFont(font4)
        self.UG_1_logo_1.setScaledContents(False)
        self.UG_1_logo_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.UG_1_logo_1)


        self.verticalLayout_16.addWidget(self.widget_11)

        self.UG_1_BG_1 = QWidget(self.UG_1)
        self.UG_1_BG_1.setObjectName(u"UG_1_BG_1")
        self.UG_1_BG_1.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_13 = QHBoxLayout(self.UG_1_BG_1)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.UG_1_BG_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/Usergate/Usergate C100.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_2)


        self.verticalLayout_16.addWidget(self.UG_1_BG_1)

        self.widget_13 = QWidget(self.UG_1)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_18 = QVBoxLayout(self.widget_13)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(50, 2, 50, 2)
        self.UG_1_add_btn_1 = QPushButton(self.widget_13)
        self.UG_1_add_btn_1.setObjectName(u"UG_1_add_btn_1")
        self.UG_1_add_btn_1.setMinimumSize(QSize(25, 20))
        self.UG_1_add_btn_1.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setFamily(u"Bookman Old Style")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.UG_1_add_btn_1.setFont(font5)
        self.UG_1_add_btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.UG_1_add_btn_1)


        self.verticalLayout_16.addWidget(self.widget_13)


        self.horizontalLayout_12.addWidget(self.UG_1)

        self.UG_2 = QWidget(self.SizeA)
        self.UG_2.setObjectName(u"UG_2")
        self.UG_2.setMinimumSize(QSize(150, 0))
        self.UG_2.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.UG_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 0, 2, 0)
        self.widget_12 = QWidget(self.UG_2)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_20 = QVBoxLayout(self.widget_12)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.UG_2_logo_2 = QLabel(self.widget_12)
        self.UG_2_logo_2.setObjectName(u"UG_2_logo_2")
        self.UG_2_logo_2.setFont(font4)
        self.UG_2_logo_2.setScaledContents(False)
        self.UG_2_logo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.UG_2_logo_2)


        self.verticalLayout_21.addWidget(self.widget_12)

        self.UG_2_BG_2 = QWidget(self.UG_2)
        self.UG_2_BG_2.setObjectName(u"UG_2_BG_2")
        self.UG_2_BG_2.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_14 = QHBoxLayout(self.UG_2_BG_2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.label_3 = QLabel(self.UG_2_BG_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/Usergate/Usergate C150.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_3)


        self.verticalLayout_21.addWidget(self.UG_2_BG_2)

        self.widget_14 = QWidget(self.UG_2)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_19 = QVBoxLayout(self.widget_14)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(50, 2, 50, 2)
        self.UG_2_add_btn_2 = QPushButton(self.widget_14)
        self.UG_2_add_btn_2.setObjectName(u"UG_2_add_btn_2")
        self.UG_2_add_btn_2.setMinimumSize(QSize(25, 20))
        self.UG_2_add_btn_2.setMaximumSize(QSize(16777215, 20))
        self.UG_2_add_btn_2.setFont(font5)
        self.UG_2_add_btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.UG_2_add_btn_2)


        self.verticalLayout_21.addWidget(self.widget_14)


        self.horizontalLayout_12.addWidget(self.UG_2)

        self.UG_3 = QWidget(self.SizeA)
        self.UG_3.setObjectName(u"UG_3")
        self.UG_3.setMinimumSize(QSize(150, 0))
        self.UG_3.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.UG_3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(2, 0, 2, 0)
        self.widget_15 = QWidget(self.UG_3)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_22 = QVBoxLayout(self.widget_15)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.UG_3_logo_3 = QLabel(self.widget_15)
        self.UG_3_logo_3.setObjectName(u"UG_3_logo_3")
        self.UG_3_logo_3.setFont(font4)
        self.UG_3_logo_3.setScaledContents(False)
        self.UG_3_logo_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.UG_3_logo_3)


        self.verticalLayout_30.addWidget(self.widget_15)

        self.UG_3_BG_3 = QWidget(self.UG_3)
        self.UG_3_BG_3.setObjectName(u"UG_3_BG_3")
        self.UG_3_BG_3.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_15 = QHBoxLayout(self.UG_3_BG_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.label_4 = QLabel(self.UG_3_BG_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/Usergate/Usergate D200-500.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_4)


        self.verticalLayout_30.addWidget(self.UG_3_BG_3)

        self.widget_16 = QWidget(self.UG_3)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_23 = QVBoxLayout(self.widget_16)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(50, 2, 50, 2)
        self.UG_3_add_btn_3 = QPushButton(self.widget_16)
        self.UG_3_add_btn_3.setObjectName(u"UG_3_add_btn_3")
        self.UG_3_add_btn_3.setMinimumSize(QSize(25, 20))
        self.UG_3_add_btn_3.setMaximumSize(QSize(16777215, 20))
        self.UG_3_add_btn_3.setFont(font5)
        self.UG_3_add_btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.UG_3_add_btn_3)


        self.verticalLayout_30.addWidget(self.widget_16)


        self.horizontalLayout_12.addWidget(self.UG_3)

        self.UG_4 = QWidget(self.SizeA)
        self.UG_4.setObjectName(u"UG_4")
        self.UG_4.setMinimumSize(QSize(150, 0))
        self.UG_4.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_31 = QVBoxLayout(self.UG_4)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(2, 0, 2, 0)
        self.widget_17 = QWidget(self.UG_4)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_24 = QVBoxLayout(self.widget_17)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.UG_4_logo_4 = QLabel(self.widget_17)
        self.UG_4_logo_4.setObjectName(u"UG_4_logo_4")
        self.UG_4_logo_4.setFont(font4)
        self.UG_4_logo_4.setScaledContents(False)
        self.UG_4_logo_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.UG_4_logo_4)


        self.verticalLayout_31.addWidget(self.widget_17)

        self.UG_4_BG_4 = QWidget(self.UG_4)
        self.UG_4_BG_4.setObjectName(u"UG_4_BG_4")
        self.UG_4_BG_4.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_16 = QHBoxLayout(self.UG_4_BG_4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.label_5 = QLabel(self.UG_4_BG_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/Usergate/Usergate D200-500.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_5)


        self.verticalLayout_31.addWidget(self.UG_4_BG_4)

        self.widget_18 = QWidget(self.UG_4)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_25 = QVBoxLayout(self.widget_18)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(50, 2, 50, 2)
        self.UG_4_add_btn_4 = QPushButton(self.widget_18)
        self.UG_4_add_btn_4.setObjectName(u"UG_4_add_btn_4")
        self.UG_4_add_btn_4.setMinimumSize(QSize(25, 20))
        self.UG_4_add_btn_4.setMaximumSize(QSize(16777215, 20))
        self.UG_4_add_btn_4.setFont(font5)
        self.UG_4_add_btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.UG_4_add_btn_4)


        self.verticalLayout_31.addWidget(self.widget_18)


        self.horizontalLayout_12.addWidget(self.UG_4)

        self.UG_5 = QWidget(self.SizeA)
        self.UG_5.setObjectName(u"UG_5")
        self.UG_5.setMinimumSize(QSize(150, 0))
        self.UG_5.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.UG_5)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(2, 0, 2, 0)
        self.widget_19 = QWidget(self.UG_5)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_26 = QVBoxLayout(self.widget_19)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.UG_5_logo_5 = QLabel(self.widget_19)
        self.UG_5_logo_5.setObjectName(u"UG_5_logo_5")
        self.UG_5_logo_5.setFont(font4)
        self.UG_5_logo_5.setScaledContents(False)
        self.UG_5_logo_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.UG_5_logo_5)


        self.verticalLayout_32.addWidget(self.widget_19)

        self.UG_5_BG_5 = QWidget(self.UG_5)
        self.UG_5_BG_5.setObjectName(u"UG_5_BG_5")
        self.UG_5_BG_5.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_17 = QHBoxLayout(self.UG_5_BG_5)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.label_6 = QLabel(self.UG_5_BG_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/Usergate/Usergate E1000-3000.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_6)


        self.verticalLayout_32.addWidget(self.UG_5_BG_5)

        self.widget_20 = QWidget(self.UG_5)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_27 = QVBoxLayout(self.widget_20)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(50, 2, 50, 2)
        self.UG_5_add_btn_5 = QPushButton(self.widget_20)
        self.UG_5_add_btn_5.setObjectName(u"UG_5_add_btn_5")
        self.UG_5_add_btn_5.setMinimumSize(QSize(25, 20))
        self.UG_5_add_btn_5.setMaximumSize(QSize(16777215, 20))
        self.UG_5_add_btn_5.setFont(font5)
        self.UG_5_add_btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.UG_5_add_btn_5)


        self.verticalLayout_32.addWidget(self.widget_20)


        self.horizontalLayout_12.addWidget(self.UG_5)

        self.UG_6 = QWidget(self.SizeA)
        self.UG_6.setObjectName(u"UG_6")
        self.UG_6.setMinimumSize(QSize(150, 0))
        self.UG_6.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_33 = QVBoxLayout(self.UG_6)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(2, 0, 2, 0)
        self.widget_21 = QWidget(self.UG_6)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_28 = QVBoxLayout(self.widget_21)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.UG_6_logo_6 = QLabel(self.widget_21)
        self.UG_6_logo_6.setObjectName(u"UG_6_logo_6")
        self.UG_6_logo_6.setFont(font4)
        self.UG_6_logo_6.setScaledContents(False)
        self.UG_6_logo_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.UG_6_logo_6)


        self.verticalLayout_33.addWidget(self.widget_21)

        self.UG_6_BG_6 = QWidget(self.UG_6)
        self.UG_6_BG_6.setObjectName(u"UG_6_BG_6")
        self.UG_6_BG_6.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_18 = QHBoxLayout(self.UG_6_BG_6)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.label_7 = QLabel(self.UG_6_BG_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/Usergate/Usergate E1000-3000.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_7)


        self.verticalLayout_33.addWidget(self.UG_6_BG_6)

        self.widget_22 = QWidget(self.UG_6)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_29 = QVBoxLayout(self.widget_22)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(50, 2, 50, 2)
        self.UG_6_add_btn_6 = QPushButton(self.widget_22)
        self.UG_6_add_btn_6.setObjectName(u"UG_6_add_btn_6")
        self.UG_6_add_btn_6.setMinimumSize(QSize(25, 20))
        self.UG_6_add_btn_6.setMaximumSize(QSize(16777215, 20))
        self.UG_6_add_btn_6.setFont(font5)
        self.UG_6_add_btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.UG_6_add_btn_6)


        self.verticalLayout_33.addWidget(self.widget_22)


        self.horizontalLayout_12.addWidget(self.UG_6)

        self.UG_7 = QWidget(self.SizeA)
        self.UG_7.setObjectName(u"UG_7")
        self.UG_7.setMinimumSize(QSize(150, 0))
        self.UG_7.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_34 = QVBoxLayout(self.UG_7)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(2, 0, 2, 0)
        self.widget_23 = QWidget(self.UG_7)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_35 = QVBoxLayout(self.widget_23)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.UG_7_logo_7 = QLabel(self.widget_23)
        self.UG_7_logo_7.setObjectName(u"UG_7_logo_7")
        self.UG_7_logo_7.setFont(font4)
        self.UG_7_logo_7.setScaledContents(False)
        self.UG_7_logo_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.UG_7_logo_7)


        self.verticalLayout_34.addWidget(self.widget_23)

        self.UG_7_BG_7 = QWidget(self.UG_7)
        self.UG_7_BG_7.setObjectName(u"UG_7_BG_7")
        self.UG_7_BG_7.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_19 = QHBoxLayout(self.UG_7_BG_7)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.label_8 = QLabel(self.UG_7_BG_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/Usergate/Usergate F8000.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_8)


        self.verticalLayout_34.addWidget(self.UG_7_BG_7)

        self.widget_24 = QWidget(self.UG_7)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_36 = QVBoxLayout(self.widget_24)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(50, 2, 50, 2)
        self.UG_7_add_btn_7 = QPushButton(self.widget_24)
        self.UG_7_add_btn_7.setObjectName(u"UG_7_add_btn_7")
        self.UG_7_add_btn_7.setMinimumSize(QSize(25, 20))
        self.UG_7_add_btn_7.setMaximumSize(QSize(16777215, 20))
        self.UG_7_add_btn_7.setFont(font5)
        self.UG_7_add_btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_36.addWidget(self.UG_7_add_btn_7)


        self.verticalLayout_34.addWidget(self.widget_24)


        self.horizontalLayout_12.addWidget(self.UG_7)

        self.UG_8 = QWidget(self.SizeA)
        self.UG_8.setObjectName(u"UG_8")
        self.UG_8.setMinimumSize(QSize(150, 0))
        self.UG_8.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_37 = QVBoxLayout(self.UG_8)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(2, 0, 2, 0)
        self.widget_25 = QWidget(self.UG_8)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_38 = QVBoxLayout(self.widget_25)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.UG_8_logo_8 = QLabel(self.widget_25)
        self.UG_8_logo_8.setObjectName(u"UG_8_logo_8")
        self.UG_8_logo_8.setFont(font4)
        self.UG_8_logo_8.setScaledContents(False)
        self.UG_8_logo_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.UG_8_logo_8)


        self.verticalLayout_37.addWidget(self.widget_25)

        self.UG_8_BG_8 = QWidget(self.UG_8)
        self.UG_8_BG_8.setObjectName(u"UG_8_BG_8")
        self.UG_8_BG_8.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_20 = QHBoxLayout(self.UG_8_BG_8)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(3, 3, 3, 3)
        self.label_9 = QLabel(self.UG_8_BG_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/Usergate/Usergate X1.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_9)


        self.verticalLayout_37.addWidget(self.UG_8_BG_8)

        self.widget_26 = QWidget(self.UG_8)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_39 = QVBoxLayout(self.widget_26)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(50, 2, 50, 2)
        self.UG_8_add_btn_8 = QPushButton(self.widget_26)
        self.UG_8_add_btn_8.setObjectName(u"UG_8_add_btn_8")
        self.UG_8_add_btn_8.setMinimumSize(QSize(25, 20))
        self.UG_8_add_btn_8.setMaximumSize(QSize(16777215, 20))
        self.UG_8_add_btn_8.setFont(font5)
        self.UG_8_add_btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_39.addWidget(self.UG_8_add_btn_8)


        self.verticalLayout_37.addWidget(self.widget_26)


        self.horizontalLayout_12.addWidget(self.UG_8)

        self.UG_9 = QWidget(self.SizeA)
        self.UG_9.setObjectName(u"UG_9")
        self.UG_9.setMinimumSize(QSize(150, 0))
        self.UG_9.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_43 = QVBoxLayout(self.UG_9)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(2, 0, 2, 0)
        self.widget_29 = QWidget(self.UG_9)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_44 = QVBoxLayout(self.widget_29)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.UG_9_logo_9 = QLabel(self.widget_29)
        self.UG_9_logo_9.setObjectName(u"UG_9_logo_9")
        self.UG_9_logo_9.setFont(font4)
        self.UG_9_logo_9.setScaledContents(False)
        self.UG_9_logo_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.UG_9_logo_9)


        self.verticalLayout_43.addWidget(self.widget_29)

        self.UG_9_BG_9 = QWidget(self.UG_9)
        self.UG_9_BG_9.setObjectName(u"UG_9_BG_9")
        self.UG_9_BG_9.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_22 = QHBoxLayout(self.UG_9_BG_9)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(3, 3, 3, 3)
        self.label_11 = QLabel(self.UG_9_BG_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/Usergate/Usergate FG.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_11)


        self.verticalLayout_43.addWidget(self.UG_9_BG_9)

        self.widget_30 = QWidget(self.UG_9)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_45 = QVBoxLayout(self.widget_30)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(50, 2, 50, 2)
        self.UG_9_add_btn_9 = QPushButton(self.widget_30)
        self.UG_9_add_btn_9.setObjectName(u"UG_9_add_btn_9")
        self.UG_9_add_btn_9.setMinimumSize(QSize(25, 20))
        self.UG_9_add_btn_9.setMaximumSize(QSize(16777215, 20))
        self.UG_9_add_btn_9.setFont(font5)
        self.UG_9_add_btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_45.addWidget(self.UG_9_add_btn_9)


        self.verticalLayout_43.addWidget(self.widget_30)


        self.horizontalLayout_12.addWidget(self.UG_9)

        self.UG_10 = QWidget(self.SizeA)
        self.UG_10.setObjectName(u"UG_10")
        self.UG_10.setMinimumSize(QSize(150, 0))
        self.UG_10.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_49 = QVBoxLayout(self.UG_10)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(2, 0, 2, 0)
        self.widget_33 = QWidget(self.UG_10)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_50 = QVBoxLayout(self.widget_33)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.UG_10_logo_10 = QLabel(self.widget_33)
        self.UG_10_logo_10.setObjectName(u"UG_10_logo_10")
        self.UG_10_logo_10.setFont(font4)
        self.UG_10_logo_10.setScaledContents(False)
        self.UG_10_logo_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.UG_10_logo_10)


        self.verticalLayout_49.addWidget(self.widget_33)

        self.UG_10_BG_10 = QWidget(self.UG_10)
        self.UG_10_BG_10.setObjectName(u"UG_10_BG_10")
        self.UG_10_BG_10.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_24 = QHBoxLayout(self.UG_10_BG_10)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(30, 3, 30, 3)
        self.label_13 = QLabel(self.UG_10_BG_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_13)


        self.verticalLayout_49.addWidget(self.UG_10_BG_10)

        self.widget_34 = QWidget(self.UG_10)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_51 = QVBoxLayout(self.widget_34)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(50, 2, 50, 2)
        self.UG_10_add_btn_10 = QPushButton(self.widget_34)
        self.UG_10_add_btn_10.setObjectName(u"UG_10_add_btn_10")
        self.UG_10_add_btn_10.setMinimumSize(QSize(25, 20))
        self.UG_10_add_btn_10.setMaximumSize(QSize(16777215, 20))
        self.UG_10_add_btn_10.setFont(font5)
        self.UG_10_add_btn_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_51.addWidget(self.UG_10_add_btn_10)


        self.verticalLayout_49.addWidget(self.widget_34)


        self.horizontalLayout_12.addWidget(self.UG_10)

        self.UG_11 = QWidget(self.SizeA)
        self.UG_11.setObjectName(u"UG_11")
        self.UG_11.setMinimumSize(QSize(150, 0))
        self.UG_11.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_52 = QVBoxLayout(self.UG_11)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(2, 0, 2, 0)
        self.widget_35 = QWidget(self.UG_11)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_53 = QVBoxLayout(self.widget_35)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.UG_11_logo_11 = QLabel(self.widget_35)
        self.UG_11_logo_11.setObjectName(u"UG_11_logo_11")
        self.UG_11_logo_11.setFont(font4)
        self.UG_11_logo_11.setScaledContents(False)
        self.UG_11_logo_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.UG_11_logo_11)


        self.verticalLayout_52.addWidget(self.widget_35)

        self.UG_11_BG_11 = QWidget(self.UG_11)
        self.UG_11_BG_11.setObjectName(u"UG_11_BG_11")
        self.UG_11_BG_11.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_25 = QHBoxLayout(self.UG_11_BG_11)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(30, 3, 30, 3)
        self.label_14 = QLabel(self.UG_11_BG_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(False)

        self.horizontalLayout_25.addWidget(self.label_14)


        self.verticalLayout_52.addWidget(self.UG_11_BG_11)

        self.widget_36 = QWidget(self.UG_11)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_54 = QVBoxLayout(self.widget_36)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(50, 2, 50, 2)
        self.UG_11_add_btn_11 = QPushButton(self.widget_36)
        self.UG_11_add_btn_11.setObjectName(u"UG_11_add_btn_11")
        self.UG_11_add_btn_11.setMinimumSize(QSize(25, 20))
        self.UG_11_add_btn_11.setMaximumSize(QSize(16777215, 20))
        self.UG_11_add_btn_11.setFont(font5)
        self.UG_11_add_btn_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_54.addWidget(self.UG_11_add_btn_11)


        self.verticalLayout_52.addWidget(self.widget_36)


        self.horizontalLayout_12.addWidget(self.UG_11)

        self.UG_12 = QWidget(self.SizeA)
        self.UG_12.setObjectName(u"UG_12")
        self.UG_12.setMinimumSize(QSize(150, 0))
        self.UG_12.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_55 = QVBoxLayout(self.UG_12)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(2, 0, 2, 0)
        self.widget_37 = QWidget(self.UG_12)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_56 = QVBoxLayout(self.widget_37)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.UG_12_logo_12 = QLabel(self.widget_37)
        self.UG_12_logo_12.setObjectName(u"UG_12_logo_12")
        self.UG_12_logo_12.setFont(font4)
        self.UG_12_logo_12.setScaledContents(False)
        self.UG_12_logo_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.UG_12_logo_12)


        self.verticalLayout_55.addWidget(self.widget_37)

        self.UG_12_BG_12 = QWidget(self.UG_12)
        self.UG_12_BG_12.setObjectName(u"UG_12_BG_12")
        self.UG_12_BG_12.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_26 = QHBoxLayout(self.UG_12_BG_12)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(30, 3, 30, 3)
        self.label_15 = QLabel(self.UG_12_BG_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_15)


        self.verticalLayout_55.addWidget(self.UG_12_BG_12)

        self.widget_38 = QWidget(self.UG_12)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_57 = QVBoxLayout(self.widget_38)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(50, 2, 50, 2)
        self.UG_12_add_btn_12 = QPushButton(self.widget_38)
        self.UG_12_add_btn_12.setObjectName(u"UG_12_add_btn_12")
        self.UG_12_add_btn_12.setMinimumSize(QSize(25, 20))
        self.UG_12_add_btn_12.setMaximumSize(QSize(16777215, 20))
        self.UG_12_add_btn_12.setFont(font5)
        self.UG_12_add_btn_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_57.addWidget(self.UG_12_add_btn_12)


        self.verticalLayout_55.addWidget(self.widget_38)


        self.horizontalLayout_12.addWidget(self.UG_12)

        self.UG_13 = QWidget(self.SizeA)
        self.UG_13.setObjectName(u"UG_13")
        self.UG_13.setMinimumSize(QSize(150, 0))
        self.UG_13.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_58 = QVBoxLayout(self.UG_13)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(2, 0, 2, 0)
        self.widget_39 = QWidget(self.UG_13)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_59 = QVBoxLayout(self.widget_39)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.UG_13_logo_13 = QLabel(self.widget_39)
        self.UG_13_logo_13.setObjectName(u"UG_13_logo_13")
        self.UG_13_logo_13.setFont(font4)
        self.UG_13_logo_13.setScaledContents(False)
        self.UG_13_logo_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.UG_13_logo_13)


        self.verticalLayout_58.addWidget(self.widget_39)

        self.UG_13_BG_13 = QWidget(self.UG_13)
        self.UG_13_BG_13.setObjectName(u"UG_13_BG_13")
        self.UG_13_BG_13.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_27 = QHBoxLayout(self.UG_13_BG_13)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(30, 3, 30, 3)
        self.label_16 = QLabel(self.UG_13_BG_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_16)


        self.verticalLayout_58.addWidget(self.UG_13_BG_13)

        self.widget_40 = QWidget(self.UG_13)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_60 = QVBoxLayout(self.widget_40)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(50, 2, 50, 2)
        self.UG_13_add_btn_13 = QPushButton(self.widget_40)
        self.UG_13_add_btn_13.setObjectName(u"UG_13_add_btn_13")
        self.UG_13_add_btn_13.setMinimumSize(QSize(25, 20))
        self.UG_13_add_btn_13.setMaximumSize(QSize(16777215, 20))
        self.UG_13_add_btn_13.setFont(font5)
        self.UG_13_add_btn_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_60.addWidget(self.UG_13_add_btn_13)


        self.verticalLayout_58.addWidget(self.widget_40)


        self.horizontalLayout_12.addWidget(self.UG_13)

        self.UG_14 = QWidget(self.SizeA)
        self.UG_14.setObjectName(u"UG_14")
        self.UG_14.setMinimumSize(QSize(150, 0))
        self.UG_14.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_64 = QVBoxLayout(self.UG_14)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(2, 0, 2, 0)
        self.widget_43 = QWidget(self.UG_14)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_65 = QVBoxLayout(self.widget_43)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.UG_14_logo_14 = QLabel(self.widget_43)
        self.UG_14_logo_14.setObjectName(u"UG_14_logo_14")
        self.UG_14_logo_14.setFont(font4)
        self.UG_14_logo_14.setScaledContents(False)
        self.UG_14_logo_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.UG_14_logo_14)


        self.verticalLayout_64.addWidget(self.widget_43)

        self.UG_14_BG_14 = QWidget(self.UG_14)
        self.UG_14_BG_14.setObjectName(u"UG_14_BG_14")
        self.UG_14_BG_14.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_29 = QHBoxLayout(self.UG_14_BG_14)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(30, 3, 30, 3)
        self.label_18 = QLabel(self.UG_14_BG_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_18)


        self.verticalLayout_64.addWidget(self.UG_14_BG_14)

        self.widget_44 = QWidget(self.UG_14)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_66 = QVBoxLayout(self.widget_44)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(50, 2, 50, 2)
        self.UG_14_add_btn_14 = QPushButton(self.widget_44)
        self.UG_14_add_btn_14.setObjectName(u"UG_14_add_btn_14")
        self.UG_14_add_btn_14.setMinimumSize(QSize(25, 20))
        self.UG_14_add_btn_14.setMaximumSize(QSize(16777215, 20))
        self.UG_14_add_btn_14.setFont(font5)
        self.UG_14_add_btn_14.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_66.addWidget(self.UG_14_add_btn_14)


        self.verticalLayout_64.addWidget(self.widget_44)


        self.horizontalLayout_12.addWidget(self.UG_14)

        self.UG_15 = QWidget(self.SizeA)
        self.UG_15.setObjectName(u"UG_15")
        self.UG_15.setMinimumSize(QSize(150, 0))
        self.UG_15.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_67 = QVBoxLayout(self.UG_15)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(2, 0, 2, 0)
        self.widget_45 = QWidget(self.UG_15)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_68 = QVBoxLayout(self.widget_45)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.UG_15_logo_15 = QLabel(self.widget_45)
        self.UG_15_logo_15.setObjectName(u"UG_15_logo_15")
        self.UG_15_logo_15.setFont(font4)
        self.UG_15_logo_15.setScaledContents(False)
        self.UG_15_logo_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.UG_15_logo_15)


        self.verticalLayout_67.addWidget(self.widget_45)

        self.UG_15_BG_15 = QWidget(self.UG_15)
        self.UG_15_BG_15.setObjectName(u"UG_15_BG_15")
        self.UG_15_BG_15.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_30 = QHBoxLayout(self.UG_15_BG_15)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(30, 3, 30, 3)
        self.label_19 = QLabel(self.UG_15_BG_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_19)


        self.verticalLayout_67.addWidget(self.UG_15_BG_15)

        self.widget_46 = QWidget(self.UG_15)
        self.widget_46.setObjectName(u"widget_46")
        self.verticalLayout_69 = QVBoxLayout(self.widget_46)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(50, 2, 50, 2)
        self.UG_15_add_btn_15 = QPushButton(self.widget_46)
        self.UG_15_add_btn_15.setObjectName(u"UG_15_add_btn_15")
        self.UG_15_add_btn_15.setMinimumSize(QSize(25, 20))
        self.UG_15_add_btn_15.setMaximumSize(QSize(16777215, 20))
        self.UG_15_add_btn_15.setFont(font5)
        self.UG_15_add_btn_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_69.addWidget(self.UG_15_add_btn_15)


        self.verticalLayout_67.addWidget(self.widget_46)


        self.horizontalLayout_12.addWidget(self.UG_15)

        self.UG_16 = QWidget(self.SizeA)
        self.UG_16.setObjectName(u"UG_16")
        self.UG_16.setMinimumSize(QSize(150, 0))
        self.UG_16.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_70 = QVBoxLayout(self.UG_16)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(2, 0, 2, 0)
        self.widget_47 = QWidget(self.UG_16)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_71 = QVBoxLayout(self.widget_47)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.UG_16_logo_16 = QLabel(self.widget_47)
        self.UG_16_logo_16.setObjectName(u"UG_16_logo_16")
        self.UG_16_logo_16.setFont(font4)
        self.UG_16_logo_16.setScaledContents(False)
        self.UG_16_logo_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.UG_16_logo_16)


        self.verticalLayout_70.addWidget(self.widget_47)

        self.UG_16_BG_16 = QWidget(self.UG_16)
        self.UG_16_BG_16.setObjectName(u"UG_16_BG_16")
        self.UG_16_BG_16.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_31 = QHBoxLayout(self.UG_16_BG_16)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(30, 3, 30, 3)
        self.label_20 = QLabel(self.UG_16_BG_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/Usergate/Usergate Virtual 100-250-500-1000-2000-4000-6000.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_20)


        self.verticalLayout_70.addWidget(self.UG_16_BG_16)

        self.widget_48 = QWidget(self.UG_16)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_72 = QVBoxLayout(self.widget_48)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(50, 2, 50, 2)
        self.UG_16_add_btn_16 = QPushButton(self.widget_48)
        self.UG_16_add_btn_16.setObjectName(u"UG_16_add_btn_16")
        self.UG_16_add_btn_16.setMinimumSize(QSize(25, 20))
        self.UG_16_add_btn_16.setMaximumSize(QSize(16777215, 20))
        self.UG_16_add_btn_16.setFont(font5)
        self.UG_16_add_btn_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_72.addWidget(self.UG_16_add_btn_16)


        self.verticalLayout_70.addWidget(self.widget_48)


        self.horizontalLayout_12.addWidget(self.UG_16)


        self.horizontalLayout_11.addWidget(self.SizeA)

        self.scrollArea.setWidget(self.scrollA)

        self.horizontalLayout_10.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.page_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.list = QWidget(self.widget_7)
        self.list.setObjectName(u"list")
        self.list.setMinimumSize(QSize(300, 0))
        self.list.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_73 = QVBoxLayout(self.list)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.list)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_88 = QVBoxLayout(self.widget_49)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.widget_63 = QWidget(self.widget_49)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(5, 0, 5, 0)
        self.widget_64 = QWidget(self.widget_63)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.File_name_logo = QLabel(self.widget_64)
        self.File_name_logo.setObjectName(u"File_name_logo")
        self.File_name_logo.setFont(font4)
        self.File_name_logo.setScaledContents(False)
        self.File_name_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.File_name_logo)


        self.horizontalLayout_34.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_63)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.File_name_edit = QLineEdit(self.widget_65)
        self.File_name_edit.setObjectName(u"File_name_edit")
        self.File_name_edit.setMinimumSize(QSize(0, 20))
        self.File_name_edit.setFont(font3)

        self.horizontalLayout_52.addWidget(self.File_name_edit)


        self.horizontalLayout_34.addWidget(self.widget_65)


        self.verticalLayout_88.addWidget(self.widget_63)

        self.treeWidget = QTreeWidget(self.widget_49)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        font6 = QFont()
        self.treeWidget.setFont(font6)
        self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.treeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)

        self.verticalLayout_88.addWidget(self.treeWidget)


        self.verticalLayout_73.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.list)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 30))
        self.widget_50.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(30, 0, 30, 0)
        self.remove_all_btn = QPushButton(self.widget_50)
        self.remove_all_btn.setObjectName(u"remove_all_btn")
        self.remove_all_btn.setMinimumSize(QSize(100, 25))
        self.remove_all_btn.setFont(font2)
        self.remove_all_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.remove_all_btn)

        self.remove_line_btn = QPushButton(self.widget_50)
        self.remove_line_btn.setObjectName(u"remove_line_btn")
        self.remove_line_btn.setMinimumSize(QSize(100, 25))
        self.remove_line_btn.setFont(font2)
        self.remove_line_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.remove_line_btn)


        self.verticalLayout_73.addWidget(self.widget_50)


        self.horizontalLayout_32.addWidget(self.list)

        self.configurator_bg = QWidget(self.widget_7)
        self.configurator_bg.setObjectName(u"configurator_bg")
        self.horizontalLayout_28 = QHBoxLayout(self.configurator_bg)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 10, 0, 0)
        self.scrollArea_2 = QScrollArea(self.configurator_bg)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollB = QWidget()
        self.scrollB.setObjectName(u"scrollB")
        self.scrollB.setGeometry(QRect(0, -185, 647, 975))
        self.scrollB.setCursor(QCursor(Qt.CrossCursor))
        self.horizontalLayout_33 = QHBoxLayout(self.scrollB)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.SizeB = QWidget(self.scrollB)
        self.SizeB.setObjectName(u"SizeB")
        self.SizeB.setMinimumSize(QSize(0, 0))
        self.SizeB.setMaximumSize(QSize(16777215, 16777215))
        self.SizeB.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_40 = QVBoxLayout(self.SizeB)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.SizeB)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 0))
        self.widget_28.setMaximumSize(QSize(16777215, 180))
        self.verticalLayout_41 = QVBoxLayout(self.widget_28)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_42 = QWidget(self.widget_28)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(0, 35))
        self.widget_42.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_42 = QVBoxLayout(self.widget_42)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(150, 1, 150, 3)
        self.Licensing_logo = QLabel(self.widget_42)
        self.Licensing_logo.setObjectName(u"Licensing_logo")
        self.Licensing_logo.setFont(font4)
        self.Licensing_logo.setScaledContents(False)
        self.Licensing_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.Licensing_logo)


        self.verticalLayout_41.addWidget(self.widget_42)

        self.Lic_bg = QWidget(self.widget_28)
        self.Lic_bg.setObjectName(u"Lic_bg")
        self.horizontalLayout_35 = QHBoxLayout(self.Lic_bg)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Lic_bg_L = QWidget(self.Lic_bg)
        self.Lic_bg_L.setObjectName(u"Lic_bg_L")
        self.horizontalLayout_36 = QHBoxLayout(self.Lic_bg_L)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_54 = QWidget(self.Lic_bg_L)
        self.widget_54.setObjectName(u"widget_54")
        self.verticalLayout_46 = QVBoxLayout(self.widget_54)
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(2, 5, 3, 5)
        self.SU_btn = QPushButton(self.widget_54)
        self.SU_btn.setObjectName(u"SU_btn")
        sizePolicy1.setHeightForWidth(self.SU_btn.sizePolicy().hasHeightForWidth())
        self.SU_btn.setSizePolicy(sizePolicy1)
        self.SU_btn.setMinimumSize(QSize(0, 30))
        self.SU_btn.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamily(u"Bookman Old Style")
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setWeight(75)
        self.SU_btn.setFont(font7)
        self.SU_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_46.addWidget(self.SU_btn)

        self.ATP_btn = QPushButton(self.widget_54)
        self.ATP_btn.setObjectName(u"ATP_btn")
        sizePolicy1.setHeightForWidth(self.ATP_btn.sizePolicy().hasHeightForWidth())
        self.ATP_btn.setSizePolicy(sizePolicy1)
        self.ATP_btn.setMinimumSize(QSize(0, 30))
        self.ATP_btn.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamily(u"Bookman Old Style")
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setWeight(75)
        font8.setStrikeOut(False)
        self.ATP_btn.setFont(font8)
        self.ATP_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_46.addWidget(self.ATP_btn)

        self.Antivirus_btn = QPushButton(self.widget_54)
        self.Antivirus_btn.setObjectName(u"Antivirus_btn")
        sizePolicy1.setHeightForWidth(self.Antivirus_btn.sizePolicy().hasHeightForWidth())
        self.Antivirus_btn.setSizePolicy(sizePolicy1)
        self.Antivirus_btn.setMinimumSize(QSize(0, 30))
        self.Antivirus_btn.setMaximumSize(QSize(16777215, 30))
        self.Antivirus_btn.setFont(font7)
        self.Antivirus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_46.addWidget(self.Antivirus_btn)

        self.Mail_btn = QPushButton(self.widget_54)
        self.Mail_btn.setObjectName(u"Mail_btn")
        sizePolicy1.setHeightForWidth(self.Mail_btn.sizePolicy().hasHeightForWidth())
        self.Mail_btn.setSizePolicy(sizePolicy1)
        self.Mail_btn.setMinimumSize(QSize(0, 30))
        self.Mail_btn.setMaximumSize(QSize(16777215, 30))
        self.Mail_btn.setFont(font7)
        self.Mail_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_46.addWidget(self.Mail_btn)


        self.horizontalLayout_36.addWidget(self.widget_54)


        self.horizontalLayout_35.addWidget(self.Lic_bg_L)

        self.Lic_bg_R = QWidget(self.Lic_bg)
        self.Lic_bg_R.setObjectName(u"Lic_bg_R")
        self.horizontalLayout_37 = QHBoxLayout(self.Lic_bg_R)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.Lic_bg_R)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_47 = QVBoxLayout(self.widget_56)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.widget_56)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_48 = QVBoxLayout(self.widget_51)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(3, 5, 2, 5)
        self.Cluster_btn = QPushButton(self.widget_51)
        self.Cluster_btn.setObjectName(u"Cluster_btn")
        sizePolicy1.setHeightForWidth(self.Cluster_btn.sizePolicy().hasHeightForWidth())
        self.Cluster_btn.setSizePolicy(sizePolicy1)
        self.Cluster_btn.setMinimumSize(QSize(0, 30))
        self.Cluster_btn.setMaximumSize(QSize(16777215, 30))
        self.Cluster_btn.setFont(font7)
        self.Cluster_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_48.addWidget(self.Cluster_btn)

        self.MGMT_btn = QPushButton(self.widget_51)
        self.MGMT_btn.setObjectName(u"MGMT_btn")
        sizePolicy1.setHeightForWidth(self.MGMT_btn.sizePolicy().hasHeightForWidth())
        self.MGMT_btn.setSizePolicy(sizePolicy1)
        self.MGMT_btn.setMinimumSize(QSize(0, 30))
        self.MGMT_btn.setMaximumSize(QSize(16777215, 30))
        self.MGMT_btn.setFont(font7)
        self.MGMT_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_48.addWidget(self.MGMT_btn)

        self.Log_btn = QPushButton(self.widget_51)
        self.Log_btn.setObjectName(u"Log_btn")
        sizePolicy1.setHeightForWidth(self.Log_btn.sizePolicy().hasHeightForWidth())
        self.Log_btn.setSizePolicy(sizePolicy1)
        self.Log_btn.setMinimumSize(QSize(0, 30))
        self.Log_btn.setMaximumSize(QSize(16777215, 30))
        self.Log_btn.setFont(font7)
        self.Log_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_48.addWidget(self.Log_btn)


        self.verticalLayout_47.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_56)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_47.addWidget(self.widget_52)


        self.horizontalLayout_37.addWidget(self.widget_56)


        self.horizontalLayout_35.addWidget(self.Lic_bg_R)


        self.verticalLayout_41.addWidget(self.Lic_bg)


        self.verticalLayout_40.addWidget(self.widget_28)

        self.widget_31 = QWidget(self.SizeB)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(0, 195))
        self.widget_31.setMaximumSize(QSize(16777215, 195))
        self.verticalLayout_61 = QVBoxLayout(self.widget_31)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.widget_55 = QWidget(self.widget_31)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setMinimumSize(QSize(0, 45))
        self.widget_55.setMaximumSize(QSize(16777215, 45))
        self.verticalLayout_62 = QVBoxLayout(self.widget_55)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(150, 10, 150, 3)
        self.Network_cards_logo = QLabel(self.widget_55)
        self.Network_cards_logo.setObjectName(u"Network_cards_logo")
        self.Network_cards_logo.setFont(font4)
        self.Network_cards_logo.setScaledContents(False)
        self.Network_cards_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.Network_cards_logo)


        self.verticalLayout_61.addWidget(self.widget_55)

        self.widget_53 = QWidget(self.widget_31)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setMinimumSize(QSize(0, 0))
        self.widget_53.setMaximumSize(QSize(16777215, 16777215))
        self.widget_53.setStyleSheet(u"")
        self.verticalLayout_63 = QVBoxLayout(self.widget_53)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(2, 0, 2, 0)
        self.scrollArea_3 = QScrollArea(self.widget_53)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollC = QWidget()
        self.scrollC.setObjectName(u"scrollC")
        self.scrollC.setGeometry(QRect(0, 0, 1645, 145))
        self.verticalLayout_74 = QVBoxLayout(self.scrollC)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.SizeC = QWidget(self.scrollC)
        self.SizeC.setObjectName(u"SizeC")
        self.SizeC.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_38 = QHBoxLayout(self.SizeC)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.interface_card_1 = QWidget(self.SizeC)
        self.interface_card_1.setObjectName(u"interface_card_1")
        self.interface_card_1.setMinimumSize(QSize(145, 145))
        self.interface_card_1.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.interface_card_1)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 2)
        self.card_1_bg_1 = QFrame(self.interface_card_1)
        self.card_1_bg_1.setObjectName(u"card_1_bg_1")
        self.card_1_bg_1.setFrameShape(QFrame.StyledPanel)
        self.card_1_bg_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.card_1_bg_1)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.card_1_bg_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 29))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_3)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.card_1_logo_1 = QLabel(self.frame_3)
        self.card_1_logo_1.setObjectName(u"card_1_logo_1")
        self.card_1_logo_1.setFont(font2)
        self.card_1_logo_1.setScaledContents(False)
        self.card_1_logo_1.setAlignment(Qt.AlignCenter)
        self.card_1_logo_1.setWordWrap(False)

        self.verticalLayout_76.addWidget(self.card_1_logo_1)


        self.verticalLayout_75.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.card_1_bg_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.card_1_btn_1 = QPushButton(self.frame_4)
        self.card_1_btn_1.setObjectName(u"card_1_btn_1")
        sizePolicy2.setHeightForWidth(self.card_1_btn_1.sizePolicy().hasHeightForWidth())
        self.card_1_btn_1.setSizePolicy(sizePolicy2)
        self.card_1_btn_1.setMinimumSize(QSize(139, 110))
        self.card_1_btn_1.setMaximumSize(QSize(16777215, 16777215))
        self.card_1_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_1_btn_1.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/img/Network_cards.png", QSize(), QIcon.Normal, QIcon.Off)
        self.card_1_btn_1.setIcon(icon4)
        self.card_1_btn_1.setIconSize(QSize(100, 100))
        self.card_1_btn_1.setAutoRepeat(False)
        self.card_1_btn_1.setAutoExclusive(True)

        self.horizontalLayout_40.addWidget(self.card_1_btn_1)


        self.verticalLayout_75.addWidget(self.frame_4)


        self.horizontalLayout_39.addWidget(self.card_1_bg_1)


        self.horizontalLayout_38.addWidget(self.interface_card_1)

        self.interface_card_2 = QWidget(self.SizeC)
        self.interface_card_2.setObjectName(u"interface_card_2")
        self.interface_card_2.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_42 = QHBoxLayout(self.interface_card_2)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 2)
        self.card_2_bg_2 = QFrame(self.interface_card_2)
        self.card_2_bg_2.setObjectName(u"card_2_bg_2")
        self.card_2_bg_2.setFrameShape(QFrame.StyledPanel)
        self.card_2_bg_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.card_2_bg_2)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.card_2_bg_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 29))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_5)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.card_2_logo_2 = QLabel(self.frame_5)
        self.card_2_logo_2.setObjectName(u"card_2_logo_2")
        self.card_2_logo_2.setFont(font2)
        self.card_2_logo_2.setScaledContents(False)
        self.card_2_logo_2.setAlignment(Qt.AlignCenter)
        self.card_2_logo_2.setWordWrap(False)

        self.verticalLayout_78.addWidget(self.card_2_logo_2)


        self.verticalLayout_77.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.card_2_bg_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.card_2_btn_2 = QPushButton(self.frame_6)
        self.card_2_btn_2.setObjectName(u"card_2_btn_2")
        sizePolicy2.setHeightForWidth(self.card_2_btn_2.sizePolicy().hasHeightForWidth())
        self.card_2_btn_2.setSizePolicy(sizePolicy2)
        self.card_2_btn_2.setMinimumSize(QSize(139, 110))
        self.card_2_btn_2.setMaximumSize(QSize(16777215, 16777215))
        self.card_2_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_2_btn_2.setIcon(icon4)
        self.card_2_btn_2.setIconSize(QSize(100, 100))
        self.card_2_btn_2.setAutoRepeat(False)
        self.card_2_btn_2.setAutoExclusive(True)

        self.horizontalLayout_41.addWidget(self.card_2_btn_2)


        self.verticalLayout_77.addWidget(self.frame_6)


        self.horizontalLayout_42.addWidget(self.card_2_bg_2)


        self.horizontalLayout_38.addWidget(self.interface_card_2)

        self.interface_card_3 = QWidget(self.SizeC)
        self.interface_card_3.setObjectName(u"interface_card_3")
        self.interface_card_3.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_46 = QHBoxLayout(self.interface_card_3)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 2)
        self.card_3_bg_3 = QFrame(self.interface_card_3)
        self.card_3_bg_3.setObjectName(u"card_3_bg_3")
        self.card_3_bg_3.setFrameShape(QFrame.StyledPanel)
        self.card_3_bg_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.card_3_bg_3)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.card_3_bg_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 29))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_7)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.card_3_logo_3 = QLabel(self.frame_7)
        self.card_3_logo_3.setObjectName(u"card_3_logo_3")
        self.card_3_logo_3.setFont(font2)
        self.card_3_logo_3.setScaledContents(False)
        self.card_3_logo_3.setAlignment(Qt.AlignCenter)
        self.card_3_logo_3.setWordWrap(False)

        self.verticalLayout_80.addWidget(self.card_3_logo_3)


        self.verticalLayout_79.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.card_3_bg_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.card_3_btn_3 = QPushButton(self.frame_8)
        self.card_3_btn_3.setObjectName(u"card_3_btn_3")
        sizePolicy2.setHeightForWidth(self.card_3_btn_3.sizePolicy().hasHeightForWidth())
        self.card_3_btn_3.setSizePolicy(sizePolicy2)
        self.card_3_btn_3.setMinimumSize(QSize(139, 110))
        self.card_3_btn_3.setMaximumSize(QSize(16777215, 16777215))
        self.card_3_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_3_btn_3.setIcon(icon4)
        self.card_3_btn_3.setIconSize(QSize(100, 100))
        self.card_3_btn_3.setAutoRepeat(False)
        self.card_3_btn_3.setAutoExclusive(True)

        self.horizontalLayout_43.addWidget(self.card_3_btn_3)


        self.verticalLayout_79.addWidget(self.frame_8)


        self.horizontalLayout_46.addWidget(self.card_3_bg_3)


        self.horizontalLayout_38.addWidget(self.interface_card_3)

        self.interface_card_4 = QWidget(self.SizeC)
        self.interface_card_4.setObjectName(u"interface_card_4")
        self.interface_card_4.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_47 = QHBoxLayout(self.interface_card_4)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 2)
        self.card_4_bg_4 = QFrame(self.interface_card_4)
        self.card_4_bg_4.setObjectName(u"card_4_bg_4")
        self.card_4_bg_4.setFrameShape(QFrame.StyledPanel)
        self.card_4_bg_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.card_4_bg_4)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.card_4_bg_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 29))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_9)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.card_4_logo_4 = QLabel(self.frame_9)
        self.card_4_logo_4.setObjectName(u"card_4_logo_4")
        self.card_4_logo_4.setFont(font2)
        self.card_4_logo_4.setScaledContents(False)
        self.card_4_logo_4.setAlignment(Qt.AlignCenter)
        self.card_4_logo_4.setWordWrap(False)

        self.verticalLayout_82.addWidget(self.card_4_logo_4)


        self.verticalLayout_81.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.card_4_bg_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.card_4_btn_4 = QPushButton(self.frame_11)
        self.card_4_btn_4.setObjectName(u"card_4_btn_4")
        sizePolicy2.setHeightForWidth(self.card_4_btn_4.sizePolicy().hasHeightForWidth())
        self.card_4_btn_4.setSizePolicy(sizePolicy2)
        self.card_4_btn_4.setMinimumSize(QSize(139, 110))
        self.card_4_btn_4.setMaximumSize(QSize(16777215, 16777215))
        self.card_4_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_4_btn_4.setIcon(icon4)
        self.card_4_btn_4.setIconSize(QSize(100, 100))
        self.card_4_btn_4.setAutoRepeat(False)
        self.card_4_btn_4.setAutoExclusive(True)

        self.horizontalLayout_44.addWidget(self.card_4_btn_4)


        self.verticalLayout_81.addWidget(self.frame_11)


        self.horizontalLayout_47.addWidget(self.card_4_bg_4)


        self.horizontalLayout_38.addWidget(self.interface_card_4)

        self.interface_card_5 = QWidget(self.SizeC)
        self.interface_card_5.setObjectName(u"interface_card_5")
        self.interface_card_5.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_48 = QHBoxLayout(self.interface_card_5)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 2)
        self.card_5_bg_5 = QFrame(self.interface_card_5)
        self.card_5_bg_5.setObjectName(u"card_5_bg_5")
        self.card_5_bg_5.setFrameShape(QFrame.StyledPanel)
        self.card_5_bg_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.card_5_bg_5)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.card_5_bg_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 29))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_12)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.card_5_logo_5 = QLabel(self.frame_12)
        self.card_5_logo_5.setObjectName(u"card_5_logo_5")
        self.card_5_logo_5.setFont(font2)
        self.card_5_logo_5.setScaledContents(False)
        self.card_5_logo_5.setAlignment(Qt.AlignCenter)
        self.card_5_logo_5.setWordWrap(False)

        self.verticalLayout_84.addWidget(self.card_5_logo_5)


        self.verticalLayout_83.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.card_5_bg_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.card_5_btn_5 = QPushButton(self.frame_13)
        self.card_5_btn_5.setObjectName(u"card_5_btn_5")
        sizePolicy2.setHeightForWidth(self.card_5_btn_5.sizePolicy().hasHeightForWidth())
        self.card_5_btn_5.setSizePolicy(sizePolicy2)
        self.card_5_btn_5.setMinimumSize(QSize(139, 110))
        self.card_5_btn_5.setMaximumSize(QSize(16777215, 16777215))
        self.card_5_btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_5_btn_5.setIcon(icon4)
        self.card_5_btn_5.setIconSize(QSize(100, 100))
        self.card_5_btn_5.setAutoRepeat(False)
        self.card_5_btn_5.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.card_5_btn_5)


        self.verticalLayout_83.addWidget(self.frame_13)


        self.horizontalLayout_48.addWidget(self.card_5_bg_5)


        self.horizontalLayout_38.addWidget(self.interface_card_5)

        self.interface_card_6 = QWidget(self.SizeC)
        self.interface_card_6.setObjectName(u"interface_card_6")
        self.interface_card_6.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_49 = QHBoxLayout(self.interface_card_6)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 2)
        self.card_6_bg_6 = QFrame(self.interface_card_6)
        self.card_6_bg_6.setObjectName(u"card_6_bg_6")
        self.card_6_bg_6.setFrameShape(QFrame.StyledPanel)
        self.card_6_bg_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.card_6_bg_6)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.card_6_bg_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 29))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_14)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.card_6_logo_6 = QLabel(self.frame_14)
        self.card_6_logo_6.setObjectName(u"card_6_logo_6")
        self.card_6_logo_6.setFont(font2)
        self.card_6_logo_6.setScaledContents(False)
        self.card_6_logo_6.setAlignment(Qt.AlignCenter)
        self.card_6_logo_6.setWordWrap(False)

        self.verticalLayout_86.addWidget(self.card_6_logo_6)


        self.verticalLayout_85.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.card_6_bg_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.card_6_btn_6 = QPushButton(self.frame_15)
        self.card_6_btn_6.setObjectName(u"card_6_btn_6")
        sizePolicy2.setHeightForWidth(self.card_6_btn_6.sizePolicy().hasHeightForWidth())
        self.card_6_btn_6.setSizePolicy(sizePolicy2)
        self.card_6_btn_6.setMinimumSize(QSize(139, 110))
        self.card_6_btn_6.setMaximumSize(QSize(16777215, 16777215))
        self.card_6_btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_6_btn_6.setIcon(icon4)
        self.card_6_btn_6.setIconSize(QSize(100, 100))
        self.card_6_btn_6.setAutoRepeat(False)
        self.card_6_btn_6.setAutoExclusive(True)

        self.horizontalLayout_50.addWidget(self.card_6_btn_6)


        self.verticalLayout_85.addWidget(self.frame_15)


        self.horizontalLayout_49.addWidget(self.card_6_bg_6)


        self.horizontalLayout_38.addWidget(self.interface_card_6)

        self.interface_card_7 = QWidget(self.SizeC)
        self.interface_card_7.setObjectName(u"interface_card_7")
        self.interface_card_7.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_53 = QHBoxLayout(self.interface_card_7)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 2)
        self.card_7_bg_7 = QFrame(self.interface_card_7)
        self.card_7_bg_7.setObjectName(u"card_7_bg_7")
        self.card_7_bg_7.setFrameShape(QFrame.StyledPanel)
        self.card_7_bg_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.card_7_bg_7)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.card_7_bg_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 29))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_18)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.card_7_logo_7 = QLabel(self.frame_18)
        self.card_7_logo_7.setObjectName(u"card_7_logo_7")
        self.card_7_logo_7.setFont(font2)
        self.card_7_logo_7.setScaledContents(False)
        self.card_7_logo_7.setAlignment(Qt.AlignCenter)
        self.card_7_logo_7.setWordWrap(False)

        self.verticalLayout_90.addWidget(self.card_7_logo_7)


        self.verticalLayout_89.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.card_7_bg_7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 0))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.card_7_btn_7 = QPushButton(self.frame_19)
        self.card_7_btn_7.setObjectName(u"card_7_btn_7")
        sizePolicy2.setHeightForWidth(self.card_7_btn_7.sizePolicy().hasHeightForWidth())
        self.card_7_btn_7.setSizePolicy(sizePolicy2)
        self.card_7_btn_7.setMinimumSize(QSize(139, 110))
        self.card_7_btn_7.setMaximumSize(QSize(16777215, 16777215))
        self.card_7_btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/img/SFP.png", QSize(), QIcon.Normal, QIcon.Off)
        self.card_7_btn_7.setIcon(icon5)
        self.card_7_btn_7.setIconSize(QSize(90, 90))
        self.card_7_btn_7.setAutoRepeat(False)
        self.card_7_btn_7.setAutoExclusive(True)

        self.horizontalLayout_54.addWidget(self.card_7_btn_7)


        self.verticalLayout_89.addWidget(self.frame_19)


        self.horizontalLayout_53.addWidget(self.card_7_bg_7)


        self.horizontalLayout_38.addWidget(self.interface_card_7)

        self.interface_card_8 = QWidget(self.SizeC)
        self.interface_card_8.setObjectName(u"interface_card_8")
        self.interface_card_8.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_57 = QHBoxLayout(self.interface_card_8)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 2)
        self.card_8_bg_8 = QFrame(self.interface_card_8)
        self.card_8_bg_8.setObjectName(u"card_8_bg_8")
        self.card_8_bg_8.setFrameShape(QFrame.StyledPanel)
        self.card_8_bg_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.card_8_bg_8)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.card_8_bg_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 29))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_22)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.card_8_logo_8 = QLabel(self.frame_22)
        self.card_8_logo_8.setObjectName(u"card_8_logo_8")
        self.card_8_logo_8.setFont(font2)
        self.card_8_logo_8.setScaledContents(False)
        self.card_8_logo_8.setAlignment(Qt.AlignCenter)
        self.card_8_logo_8.setWordWrap(False)

        self.verticalLayout_94.addWidget(self.card_8_logo_8)


        self.verticalLayout_93.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.card_8_bg_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.card_8_btn_8 = QPushButton(self.frame_23)
        self.card_8_btn_8.setObjectName(u"card_8_btn_8")
        sizePolicy2.setHeightForWidth(self.card_8_btn_8.sizePolicy().hasHeightForWidth())
        self.card_8_btn_8.setSizePolicy(sizePolicy2)
        self.card_8_btn_8.setMinimumSize(QSize(139, 110))
        self.card_8_btn_8.setMaximumSize(QSize(16777215, 16777215))
        self.card_8_btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_8_btn_8.setIcon(icon5)
        self.card_8_btn_8.setIconSize(QSize(90, 90))
        self.card_8_btn_8.setAutoRepeat(False)
        self.card_8_btn_8.setAutoExclusive(True)

        self.horizontalLayout_58.addWidget(self.card_8_btn_8)


        self.verticalLayout_93.addWidget(self.frame_23)


        self.horizontalLayout_57.addWidget(self.card_8_bg_8)


        self.horizontalLayout_38.addWidget(self.interface_card_8)

        self.interface_card_9 = QWidget(self.SizeC)
        self.interface_card_9.setObjectName(u"interface_card_9")
        self.interface_card_9.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_59 = QHBoxLayout(self.interface_card_9)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 2)
        self.card_9_bg_9 = QFrame(self.interface_card_9)
        self.card_9_bg_9.setObjectName(u"card_9_bg_9")
        self.card_9_bg_9.setFrameShape(QFrame.StyledPanel)
        self.card_9_bg_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.card_9_bg_9)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.card_9_bg_9)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 29))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_24)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.card_9_logo_9 = QLabel(self.frame_24)
        self.card_9_logo_9.setObjectName(u"card_9_logo_9")
        self.card_9_logo_9.setFont(font2)
        self.card_9_logo_9.setScaledContents(False)
        self.card_9_logo_9.setAlignment(Qt.AlignCenter)
        self.card_9_logo_9.setWordWrap(False)

        self.verticalLayout_96.addWidget(self.card_9_logo_9)


        self.verticalLayout_95.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.card_9_bg_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 0))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.card_9_btn_9 = QPushButton(self.frame_25)
        self.card_9_btn_9.setObjectName(u"card_9_btn_9")
        sizePolicy2.setHeightForWidth(self.card_9_btn_9.sizePolicy().hasHeightForWidth())
        self.card_9_btn_9.setSizePolicy(sizePolicy2)
        self.card_9_btn_9.setMinimumSize(QSize(139, 110))
        self.card_9_btn_9.setMaximumSize(QSize(16777215, 16777215))
        self.card_9_btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_9_btn_9.setIcon(icon5)
        self.card_9_btn_9.setIconSize(QSize(90, 90))
        self.card_9_btn_9.setAutoRepeat(False)
        self.card_9_btn_9.setAutoExclusive(True)

        self.horizontalLayout_60.addWidget(self.card_9_btn_9)


        self.verticalLayout_95.addWidget(self.frame_25)


        self.horizontalLayout_59.addWidget(self.card_9_bg_9)


        self.horizontalLayout_38.addWidget(self.interface_card_9)

        self.interface_card_10 = QWidget(self.SizeC)
        self.interface_card_10.setObjectName(u"interface_card_10")
        self.interface_card_10.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_61 = QHBoxLayout(self.interface_card_10)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 2)
        self.card_10_bg_10 = QFrame(self.interface_card_10)
        self.card_10_bg_10.setObjectName(u"card_10_bg_10")
        self.card_10_bg_10.setFrameShape(QFrame.StyledPanel)
        self.card_10_bg_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.card_10_bg_10)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.card_10_bg_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 29))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_26)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.card_10_logo_10 = QLabel(self.frame_26)
        self.card_10_logo_10.setObjectName(u"card_10_logo_10")
        self.card_10_logo_10.setFont(font2)
        self.card_10_logo_10.setScaledContents(False)
        self.card_10_logo_10.setAlignment(Qt.AlignCenter)
        self.card_10_logo_10.setWordWrap(False)

        self.verticalLayout_98.addWidget(self.card_10_logo_10)


        self.verticalLayout_97.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.card_10_bg_10)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.card_10_btn_10 = QPushButton(self.frame_27)
        self.card_10_btn_10.setObjectName(u"card_10_btn_10")
        sizePolicy2.setHeightForWidth(self.card_10_btn_10.sizePolicy().hasHeightForWidth())
        self.card_10_btn_10.setSizePolicy(sizePolicy2)
        self.card_10_btn_10.setMinimumSize(QSize(139, 110))
        self.card_10_btn_10.setMaximumSize(QSize(16777215, 16777215))
        self.card_10_btn_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_10_btn_10.setIcon(icon5)
        self.card_10_btn_10.setIconSize(QSize(90, 90))
        self.card_10_btn_10.setAutoRepeat(False)
        self.card_10_btn_10.setAutoExclusive(True)

        self.horizontalLayout_62.addWidget(self.card_10_btn_10)


        self.verticalLayout_97.addWidget(self.frame_27)


        self.horizontalLayout_61.addWidget(self.card_10_bg_10)


        self.horizontalLayout_38.addWidget(self.interface_card_10)

        self.interface_card_11 = QWidget(self.SizeC)
        self.interface_card_11.setObjectName(u"interface_card_11")
        self.interface_card_11.setMinimumSize(QSize(145, 145))
        self.horizontalLayout_63 = QHBoxLayout(self.interface_card_11)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 2)
        self.card_11_bg_11 = QFrame(self.interface_card_11)
        self.card_11_bg_11.setObjectName(u"card_11_bg_11")
        self.card_11_bg_11.setFrameShape(QFrame.StyledPanel)
        self.card_11_bg_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.card_11_bg_11)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.card_11_bg_11)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 29))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_28)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.card_11_logo_11 = QLabel(self.frame_28)
        self.card_11_logo_11.setObjectName(u"card_11_logo_11")
        self.card_11_logo_11.setFont(font2)
        self.card_11_logo_11.setScaledContents(False)
        self.card_11_logo_11.setAlignment(Qt.AlignCenter)
        self.card_11_logo_11.setWordWrap(False)

        self.verticalLayout_100.addWidget(self.card_11_logo_11)


        self.verticalLayout_99.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.card_11_bg_11)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.card_11_btn_11 = QPushButton(self.frame_29)
        self.card_11_btn_11.setObjectName(u"card_11_btn_11")
        sizePolicy2.setHeightForWidth(self.card_11_btn_11.sizePolicy().hasHeightForWidth())
        self.card_11_btn_11.setSizePolicy(sizePolicy2)
        self.card_11_btn_11.setMinimumSize(QSize(139, 110))
        self.card_11_btn_11.setMaximumSize(QSize(16777215, 16777215))
        self.card_11_btn_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.card_11_btn_11.setIcon(icon5)
        self.card_11_btn_11.setIconSize(QSize(90, 90))
        self.card_11_btn_11.setAutoRepeat(False)
        self.card_11_btn_11.setAutoExclusive(True)

        self.horizontalLayout_64.addWidget(self.card_11_btn_11)


        self.verticalLayout_99.addWidget(self.frame_29)


        self.horizontalLayout_63.addWidget(self.card_11_bg_11)


        self.horizontalLayout_38.addWidget(self.interface_card_11)


        self.verticalLayout_74.addWidget(self.SizeC)

        self.scrollArea_3.setWidget(self.scrollC)

        self.verticalLayout_63.addWidget(self.scrollArea_3)


        self.verticalLayout_61.addWidget(self.widget_53)


        self.verticalLayout_40.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.SizeB)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 100))
        self.widget_32.setMaximumSize(QSize(16777215, 16777215))
        self.widget_32.setStyleSheet(u"")
        self.verticalLayout_101 = QVBoxLayout(self.widget_32)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_32)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_102 = QVBoxLayout(self.widget_10)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(150, 10, 150, 3)
        self.FSTEC_logo = QLabel(self.widget_10)
        self.FSTEC_logo.setObjectName(u"FSTEC_logo")
        self.FSTEC_logo.setFont(font4)
        self.FSTEC_logo.setScaledContents(False)
        self.FSTEC_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.FSTEC_logo)


        self.verticalLayout_101.addWidget(self.widget_10)

        self.widget_27 = QWidget(self.widget_32)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.widget_57 = QWidget(self.widget_27)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_66 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.widget_88 = QWidget(self.widget_57)
        self.widget_88.setObjectName(u"widget_88")
        self.widget_88.setMaximumSize(QSize(160, 50))
        self.horizontalLayout_86 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.check_yes = QCheckBox(self.widget_88)
        self.check_yes.setObjectName(u"check_yes")
        self.check_yes.setMaximumSize(QSize(19, 19))
        self.check_yes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_86.addWidget(self.check_yes)

        self.UG_yes = QLabel(self.widget_88)
        self.UG_yes.setObjectName(u"UG_yes")
        self.UG_yes.setMaximumSize(QSize(70, 16777215))
        self.UG_yes.setFont(font4)
        self.UG_yes.setScaledContents(False)
        self.UG_yes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.UG_yes)


        self.horizontalLayout_66.addWidget(self.widget_88)

        self.widget_89 = QWidget(self.widget_57)
        self.widget_89.setObjectName(u"widget_89")

        self.horizontalLayout_66.addWidget(self.widget_89)


        self.horizontalLayout_65.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.widget_27)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.widget_87 = QWidget(self.widget_58)
        self.widget_87.setObjectName(u"widget_87")
        self.widget_87.setMaximumSize(QSize(160, 50))
        self.horizontalLayout_85 = QHBoxLayout(self.widget_87)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.UG_no = QLabel(self.widget_87)
        self.UG_no.setObjectName(u"UG_no")
        self.UG_no.setMinimumSize(QSize(0, 0))
        self.UG_no.setMaximumSize(QSize(70, 16777215))
        self.UG_no.setFont(font4)
        self.UG_no.setLayoutDirection(Qt.LeftToRight)
        self.UG_no.setScaledContents(False)
        self.UG_no.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.UG_no)

        self.check_no = QCheckBox(self.widget_87)
        self.check_no.setObjectName(u"check_no")
        self.check_no.setMaximumSize(QSize(19, 19))
        self.check_no.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_85.addWidget(self.check_no)


        self.horizontalLayout_67.addWidget(self.widget_87)

        self.widget_86 = QWidget(self.widget_58)
        self.widget_86.setObjectName(u"widget_86")

        self.horizontalLayout_67.addWidget(self.widget_86)


        self.horizontalLayout_65.addWidget(self.widget_58)


        self.verticalLayout_101.addWidget(self.widget_27)


        self.verticalLayout_40.addWidget(self.widget_32)

        self.widget_41 = QWidget(self.SizeB)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMinimumSize(QSize(0, 100))
        self.widget_41.setStyleSheet(u"")
        self.verticalLayout_103 = QVBoxLayout(self.widget_41)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.widget_59 = QWidget(self.widget_41)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.widget_61 = QWidget(self.widget_59)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_104 = QVBoxLayout(self.widget_61)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(150, 10, 150, 3)
        self.Moduls_data_logo = QLabel(self.widget_61)
        self.Moduls_data_logo.setObjectName(u"Moduls_data_logo")
        self.Moduls_data_logo.setFont(font4)
        self.Moduls_data_logo.setScaledContents(False)
        self.Moduls_data_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_104.addWidget(self.Moduls_data_logo)


        self.horizontalLayout_68.addWidget(self.widget_61)


        self.verticalLayout_103.addWidget(self.widget_59)

        self.widget_60 = QWidget(self.widget_41)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_69 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.widget_81 = QWidget(self.widget_60)
        self.widget_81.setObjectName(u"widget_81")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.widget_84 = QWidget(self.widget_81)
        self.widget_84.setObjectName(u"widget_84")

        self.horizontalLayout_82.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.widget_81)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setMaximumSize(QSize(100, 50))
        self.horizontalLayout_84 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.yearBox = QSpinBox(self.widget_85)
        self.yearBox.setObjectName(u"yearBox")
        self.yearBox.setMaximumSize(QSize(50, 22))
        font9 = QFont()
        font9.setFamily(u"Bookman Old Style")
        font9.setBold(True)
        font9.setWeight(75)
        self.yearBox.setFont(font9)
        self.yearBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.yearBox.setMinimum(1)
        self.yearBox.setMaximum(10)

        self.horizontalLayout_84.addWidget(self.yearBox)


        self.horizontalLayout_82.addWidget(self.widget_85)


        self.horizontalLayout_69.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_60)
        self.widget_82.setObjectName(u"widget_82")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.year_name = QLabel(self.widget_82)
        self.year_name.setObjectName(u"year_name")
        self.year_name.setMaximumSize(QSize(100, 50))
        self.year_name.setFont(font4)

        self.horizontalLayout_83.addWidget(self.year_name)

        self.widget_83 = QWidget(self.widget_82)
        self.widget_83.setObjectName(u"widget_83")

        self.horizontalLayout_83.addWidget(self.widget_83)


        self.horizontalLayout_69.addWidget(self.widget_82)


        self.verticalLayout_103.addWidget(self.widget_60)


        self.verticalLayout_40.addWidget(self.widget_41)

        self.widget_62 = QWidget(self.SizeB)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setMinimumSize(QSize(0, 100))
        self.widget_62.setStyleSheet(u"")
        self.verticalLayout_107 = QVBoxLayout(self.widget_62)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.widget_66 = QWidget(self.widget_62)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_72 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.widget_67 = QWidget(self.widget_66)
        self.widget_67.setObjectName(u"widget_67")
        self.verticalLayout_108 = QVBoxLayout(self.widget_67)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(150, 10, 150, 3)
        self.TP_logo = QLabel(self.widget_67)
        self.TP_logo.setObjectName(u"TP_logo")
        self.TP_logo.setFont(font4)
        self.TP_logo.setScaledContents(False)
        self.TP_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_108.addWidget(self.TP_logo)


        self.horizontalLayout_72.addWidget(self.widget_67)


        self.verticalLayout_107.addWidget(self.widget_66)

        self.widget_68 = QWidget(self.widget_62)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_73 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.widget_74 = QWidget(self.widget_68)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_112 = QVBoxLayout(self.widget_74)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.widget_75 = QWidget(self.widget_74)
        self.widget_75.setObjectName(u"widget_75")
        self.horizontalLayout_76 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.widget_77 = QWidget(self.widget_75)
        self.widget_77.setObjectName(u"widget_77")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_77)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.standart = QLabel(self.widget_77)
        self.standart.setObjectName(u"standart")
        self.standart.setFont(font4)
        self.standart.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.standart)


        self.horizontalLayout_76.addWidget(self.widget_77)

        self.widget_78 = QWidget(self.widget_75)
        self.widget_78.setObjectName(u"widget_78")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_78)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.premium = QLabel(self.widget_78)
        self.premium.setObjectName(u"premium")
        self.premium.setFont(font4)
        self.premium.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.premium)


        self.horizontalLayout_76.addWidget(self.widget_78)


        self.verticalLayout_112.addWidget(self.widget_75)

        self.widget_76 = QWidget(self.widget_74)
        self.widget_76.setObjectName(u"widget_76")
        self.widget_76.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_77 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.widget_79 = QWidget(self.widget_76)
        self.widget_79.setObjectName(u"widget_79")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.standart_checkBox = QCheckBox(self.widget_79)
        self.standart_checkBox.setObjectName(u"standart_checkBox")
        self.standart_checkBox.setMaximumSize(QSize(19, 19))
        self.standart_checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.standart_checkBox.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_81.addWidget(self.standart_checkBox)


        self.horizontalLayout_77.addWidget(self.widget_79)

        self.widget_80 = QWidget(self.widget_76)
        self.widget_80.setObjectName(u"widget_80")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_80)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.premium_checkBox = QCheckBox(self.widget_80)
        self.premium_checkBox.setObjectName(u"premium_checkBox")
        self.premium_checkBox.setMaximumSize(QSize(19, 19))
        self.premium_checkBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_80.addWidget(self.premium_checkBox)


        self.horizontalLayout_77.addWidget(self.widget_80)


        self.verticalLayout_112.addWidget(self.widget_76)


        self.horizontalLayout_73.addWidget(self.widget_74)

        self.widget_73 = QWidget(self.widget_68)
        self.widget_73.setObjectName(u"widget_73")
        self.widget_73.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_75 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.yearBox_tp = QSpinBox(self.widget_73)
        self.yearBox_tp.setObjectName(u"yearBox_tp")
        self.yearBox_tp.setMaximumSize(QSize(50, 22))
        self.yearBox_tp.setFont(font9)
        self.yearBox_tp.setCursor(QCursor(Qt.PointingHandCursor))
        self.yearBox_tp.setReadOnly(False)
        self.yearBox_tp.setMinimum(1)
        self.yearBox_tp.setMaximum(10)

        self.horizontalLayout_75.addWidget(self.yearBox_tp)

        self.year_name_3 = QLabel(self.widget_73)
        self.year_name_3.setObjectName(u"year_name_3")
        self.year_name_3.setMaximumSize(QSize(100, 50))
        self.year_name_3.setFont(font4)

        self.horizontalLayout_75.addWidget(self.year_name_3)


        self.horizontalLayout_73.addWidget(self.widget_73)


        self.verticalLayout_107.addWidget(self.widget_68)


        self.verticalLayout_40.addWidget(self.widget_62)

        self.widget_69 = QWidget(self.SizeB)
        self.widget_69.setObjectName(u"widget_69")
        self.widget_69.setMinimumSize(QSize(0, 300))
        self.widget_69.setStyleSheet(u"")
        self.verticalLayout_109 = QVBoxLayout(self.widget_69)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.widget_70 = QWidget(self.widget_69)
        self.widget_70.setObjectName(u"widget_70")
        self.widget_70.setMinimumSize(QSize(0, 50))
        self.widget_70.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_74 = QHBoxLayout(self.widget_70)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(150, 10, 150, 3)
        self.widget_71 = QWidget(self.widget_70)
        self.widget_71.setObjectName(u"widget_71")
        self.widget_71.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_110 = QVBoxLayout(self.widget_71)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.Comments_logo = QLabel(self.widget_71)
        self.Comments_logo.setObjectName(u"Comments_logo")
        self.Comments_logo.setFont(font4)
        self.Comments_logo.setScaledContents(False)
        self.Comments_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_110.addWidget(self.Comments_logo)


        self.horizontalLayout_74.addWidget(self.widget_71)


        self.verticalLayout_109.addWidget(self.widget_70)

        self.widget_72 = QWidget(self.widget_69)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_111 = QVBoxLayout(self.widget_72)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(20, 5, 20, 5)
        self.comentEdit = QTextEdit(self.widget_72)
        self.comentEdit.setObjectName(u"comentEdit")
        self.comentEdit.setFont(font4)
        self.comentEdit.setAutoFillBackground(False)
        self.comentEdit.setAutoFormatting(QTextEdit.AutoAll)
        self.comentEdit.setTabChangesFocus(True)
        self.comentEdit.setLineWrapColumnOrWidth(1)
        self.comentEdit.setOverwriteMode(False)
        self.comentEdit.setTabStopWidth(100)
        self.comentEdit.setCursorWidth(1)

        self.verticalLayout_111.addWidget(self.comentEdit)


        self.verticalLayout_109.addWidget(self.widget_72)


        self.verticalLayout_40.addWidget(self.widget_69)


        self.horizontalLayout_33.addWidget(self.SizeB)

        self.scrollArea_2.setWidget(self.scrollB)

        self.horizontalLayout_28.addWidget(self.scrollArea_2)


        self.horizontalLayout_32.addWidget(self.configurator_bg)


        self.verticalLayout_13.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.page_2)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_113 = QVBoxLayout(self.page_10)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.page_10)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollE = QWidget()
        self.scrollE.setObjectName(u"scrollE")
        self.scrollE.setGeometry(QRect(0, 0, 952, 507))
        self.horizontalLayout_94 = QHBoxLayout(self.scrollE)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.SizeE = QWidget(self.scrollE)
        self.SizeE.setObjectName(u"SizeE")

        self.horizontalLayout_94.addWidget(self.SizeE)

        self.scrollArea_5.setWidget(self.scrollE)

        self.verticalLayout_113.addWidget(self.scrollArea_5)

        self.widget_97 = QWidget(self.page_10)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setMinimumSize(QSize(0, 30))
        self.widget_97.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_89 = QHBoxLayout(self.widget_97)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.widget_98 = QWidget(self.widget_97)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMinimumSize(QSize(200, 0))
        self.widget_98.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_89.addWidget(self.widget_98)

        self.widget_99 = QWidget(self.widget_97)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMinimumSize(QSize(400, 0))
        self.horizontalLayout_90 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 2, 0, 2)
        self.progressBar_download = QProgressBar(self.widget_99)
        self.progressBar_download.setObjectName(u"progressBar_download")
        self.progressBar_download.setMinimumSize(QSize(0, 20))
        self.progressBar_download.setMaximumSize(QSize(16777215, 20))
        self.progressBar_download.setFont(font2)
        self.progressBar_download.setLayoutDirection(Qt.LeftToRight)
        self.progressBar_download.setMinimum(0)
        self.progressBar_download.setValue(0)
        self.progressBar_download.setAlignment(Qt.AlignCenter)
        self.progressBar_download.setTextVisible(True)
        self.progressBar_download.setOrientation(Qt.Horizontal)
        self.progressBar_download.setInvertedAppearance(False)
        self.progressBar_download.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_90.addWidget(self.progressBar_download)


        self.horizontalLayout_89.addWidget(self.widget_99)

        self.widget_100 = QWidget(self.widget_97)
        self.widget_100.setObjectName(u"widget_100")
        self.widget_100.setMinimumSize(QSize(200, 0))
        self.widget_100.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_89.addWidget(self.widget_100)


        self.verticalLayout_113.addWidget(self.widget_97)

        self.stackedWidget.addWidget(self.page_10)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.main_stacked)


        self.verticalLayout.addWidget(self.mid)

        self.down = QWidget(self.mainR)
        self.down.setObjectName(u"down")
        self.down.setMinimumSize(QSize(0, 15))
        self.down.setMaximumSize(QSize(16777215, 15))
        self.horizontalLayout_87 = QHBoxLayout(self.down)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.widget_90 = QWidget(self.down)
        self.widget_90.setObjectName(u"widget_90")

        self.horizontalLayout_87.addWidget(self.widget_90)

        self.resize_zone = QWidget(self.down)
        self.resize_zone.setObjectName(u"resize_zone")
        self.resize_zone.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_87.addWidget(self.resize_zone)


        self.verticalLayout.addWidget(self.down)


        self.horizontalLayout.addWidget(self.mainR)


        self.horizontalLayout_23.addWidget(self.main)

        MainWindow.setCentralWidget(self.Stilesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainFunction_btn.setText(QCoreApplication.translate("MainWindow", u"Main Function", None))
        self.Usergate_btn.setText(QCoreApplication.translate("MainWindow", u"Usergate Creator", None))
        self.Documents_btn.setText(QCoreApplication.translate("MainWindow", u"Documents", None))
        self.FTP_status_text.setText(QCoreApplication.translate("MainWindow", u"FTP status", None))
        self.Status_ico.setText("")
        self.roll_btn.setText("")
        self.resize_btn.setText("")
        self.clouse_btn.setText("")
        self.openMenu_btn.setText("")
#if QT_CONFIG(shortcut)
        self.openMenu_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.FTP_connections_logo.setText(QCoreApplication.translate("MainWindow", u"FTP connections", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.UG_1_logo_1.setText(QCoreApplication.translate("MainWindow", u"Usergate C100", None))
        self.label_2.setText("")
        self.UG_1_add_btn_1.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_2_logo_2.setText(QCoreApplication.translate("MainWindow", u"Usergate C150", None))
        self.label_3.setText("")
        self.UG_2_add_btn_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_3_logo_3.setText(QCoreApplication.translate("MainWindow", u"Usergate D200", None))
        self.label_4.setText("")
        self.UG_3_add_btn_3.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_4_logo_4.setText(QCoreApplication.translate("MainWindow", u"Usergate D500", None))
        self.label_5.setText("")
        self.UG_4_add_btn_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_5_logo_5.setText(QCoreApplication.translate("MainWindow", u"Usergate E1000", None))
        self.label_6.setText("")
        self.UG_5_add_btn_5.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_6_logo_6.setText(QCoreApplication.translate("MainWindow", u"Usergate E3000", None))
        self.label_7.setText("")
        self.UG_6_add_btn_6.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_7_logo_7.setText(QCoreApplication.translate("MainWindow", u"Usergate F8000", None))
        self.label_8.setText("")
        self.UG_7_add_btn_7.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_8_logo_8.setText(QCoreApplication.translate("MainWindow", u"Usergate X1", None))
        self.label_9.setText("")
        self.UG_8_add_btn_8.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_9_logo_9.setText(QCoreApplication.translate("MainWindow", u"Usergate FG", None))
        self.label_11.setText("")
        self.UG_9_add_btn_9.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_10_logo_10.setText(QCoreApplication.translate("MainWindow", u"Usergate VE100", None))
        self.label_13.setText("")
        self.UG_10_add_btn_10.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_11_logo_11.setText(QCoreApplication.translate("MainWindow", u"Usergate VE250", None))
        self.label_14.setText("")
        self.UG_11_add_btn_11.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_12_logo_12.setText(QCoreApplication.translate("MainWindow", u"Usergate VE500", None))
        self.label_15.setText("")
        self.UG_12_add_btn_12.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_13_logo_13.setText(QCoreApplication.translate("MainWindow", u"Usergate VE1000", None))
        self.label_16.setText("")
        self.UG_13_add_btn_13.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_14_logo_14.setText(QCoreApplication.translate("MainWindow", u"Usergate VE2000", None))
        self.label_18.setText("")
        self.UG_14_add_btn_14.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_15_logo_15.setText(QCoreApplication.translate("MainWindow", u"Usergate VE4000", None))
        self.label_19.setText("")
        self.UG_15_add_btn_15.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.UG_16_logo_16.setText(QCoreApplication.translate("MainWindow", u"Usergate VE6000", None))
        self.label_20.setText("")
        self.UG_16_add_btn_16.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.File_name_logo.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.remove_all_btn.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.remove_line_btn.setText(QCoreApplication.translate("MainWindow", u"Remove line", None))
        self.Licensing_logo.setText(QCoreApplication.translate("MainWindow", u"Licensing", None))
        self.SU_btn.setText(QCoreApplication.translate("MainWindow", u"Security Updates (SU)", None))
        self.ATP_btn.setText(QCoreApplication.translate("MainWindow", u"Advanced Threat Protection (ATP)", None))
        self.Antivirus_btn.setText(QCoreApplication.translate("MainWindow", u"Streaming antivirus", None))
        self.Mail_btn.setText(QCoreApplication.translate("MainWindow", u"Mail Security", None))
        self.Cluster_btn.setText(QCoreApplication.translate("MainWindow", u"Cluster", None))
        self.MGMT_btn.setText(QCoreApplication.translate("MainWindow", u"Management Center (Lic)", None))
        self.Log_btn.setText(QCoreApplication.translate("MainWindow", u"Log Analyzer (Lic)", None))
        self.Network_cards_logo.setText(QCoreApplication.translate("MainWindow", u"Network cards and moduls", None))
        self.card_1_logo_1.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 8*1 GB/s", None))
        self.card_2_logo_2.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 4*1 GB/s", None))
        self.card_2_btn_2.setText("")
        self.card_3_logo_3.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 4*1 GB/s (FO)", None))
        self.card_3_btn_3.setText("")
        self.card_4_logo_4.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 4*10 GB/s", None))
        self.card_4_btn_4.setText("")
        self.card_5_logo_5.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 4*10 GB/s (FO)", None))
        self.card_5_btn_5.setText("")
        self.card_6_logo_6.setText(QCoreApplication.translate("MainWindow", u"\u0421ard 1*40 GB/s", None))
        self.card_6_btn_6.setText("")
        self.card_7_logo_7.setText(QCoreApplication.translate("MainWindow", u"SFP-RJ-45 1G", None))
        self.card_7_btn_7.setText("")
        self.card_8_logo_8.setText(QCoreApplication.translate("MainWindow", u"SFP+ 10G", None))
        self.card_8_btn_8.setText("")
        self.card_9_logo_9.setText(QCoreApplication.translate("MainWindow", u"SFP+ 10Gb, 500m", None))
        self.card_9_btn_9.setText("")
        self.card_10_logo_10.setText(QCoreApplication.translate("MainWindow", u"SFP 10Gb, 10km", None))
        self.card_10_btn_10.setText("")
        self.card_11_logo_11.setText(QCoreApplication.translate("MainWindow", u"SFP-SX-1,25", None))
        self.card_11_btn_11.setText("")
        self.FSTEC_logo.setText(QCoreApplication.translate("MainWindow", u"FSTEC Certificate", None))
        self.check_yes.setText("")
        self.UG_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.UG_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.check_no.setText("")
        self.Moduls_data_logo.setText(QCoreApplication.translate("MainWindow", u"Period for module subscriptions", None))
        self.year_name.setText(QCoreApplication.translate("MainWindow", u"Years", None))
        self.TP_logo.setText(QCoreApplication.translate("MainWindow", u"Duration and type of technical support", None))
        self.standart.setText(QCoreApplication.translate("MainWindow", u"Standart", None))
        self.premium.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.standart_checkBox.setText("")
        self.premium_checkBox.setText("")
        self.year_name_3.setText(QCoreApplication.translate("MainWindow", u"Years", None))
        self.Comments_logo.setText(QCoreApplication.translate("MainWindow", u"Comment on the specification", None))
        self.comentEdit.setDocumentTitle("")
    # retranslateUi

