##############################################################################
####Imports lib###
from PySide2 import QtCore, QtWidgets, QtGui
import sys,os
##############################################################################
###Import interface file###
from interface_ui import *
from Custom_Widgets import *
#MAIN init  
class Documents_Functions(QMainWindow):
    def __init__(self, object1):
        QMainWindow.__init__(self)
        self.documents_func = object1